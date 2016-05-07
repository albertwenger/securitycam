import tornado.ioloop
import tornado.web
import logging
import json
from clarifai.client import ClarifaiApi

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html");


class ZiggeoHandler(tornado.web.RequestHandler):

    def post(self):
        event_type  = self.get_argument("event_type")
	logging.warning("Event type:" + event_type)
	if (event_type == "video_ready"):
	    data = json.loads(self.get_argument("data"))
 	    video_url = data["video"]["embed_video_url"]
	    logging.warning("Video url:" + video_url)
            clarifai_api = ClarifaiApi()
	    result = clarifai_api.tag_image_urls(video_url)
	    logging.warning(result)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	(r"/ziggeo", ZiggeoHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

