import tornado.ioloop
import tornado.web
import logging
import json
import os
from clarifai.client import ClarifaiApi
from twilio.rest import TwilioRestClient 
 

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html");


class ZiggeoHandler(tornado.web.RequestHandler):

    def alert(self, video_url):
        TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
        TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
        client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            to = "+19173851022",
            from_ = "+16462332156",
            body = "Person detected, view video http://" +  video_url + ".mp4",
        )


    def analyze(self, video_url):
        clarifai_api = ClarifaiApi()
        result = clarifai_api.tag_image_urls("http://" + video_url + ".mp4")
        # logging.warning(result)
        timestamps = result["results"][0]["result"]["tag"]["timestamps"]
        classes = result["results"][0]["result"]["tag"]["classes"]
        probs = result["results"][0]["result"]["tag"]["probs"]
        discovered = False
        for ts_i, ts_v in enumerate(timestamps):
            # print "Timestamp: " + str(ts_v)
            for class_i, class_v in enumerate(classes[ts_i]):
		prob_v = probs[ts_i][class_i]
                # print "Class: " + class_v + " Prob: " + str(prob_v)
		if (class_v == "people" and prob_v >= 0.9):
                    logging.warning("Discovered a person")
                    discovered = True
        if (discovered):
            self.alert(video_url)


    def post(self):
        event_type  = self.get_argument("event_type")
	logging.warning("Event type:" + event_type)
	if (event_type == "video_ready"):
	    data = json.loads(self.get_argument("data"))
 	    video_url = data["video"]["embed_video_url"]
	    logging.warning("Video url:" + video_url)
	    self.analyze(video_url)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	(r"/ziggeo", ZiggeoHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

