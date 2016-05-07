from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi()
result = clarifai_api.tag_image_urls('http://embed.ziggeo.com/v1/applications/13234d4509cd5858e459a24e1494520d/videos/d75a98bf57a4a2c0cf225f057b545bd0/video.mp4')
# print result

timestamps = result["results"][0]["result"]["tag"]["timestamps"]
classes = result["results"][0]["result"]["tag"]["classes"]
probs = result["results"][0]["result"]["tag"]["probs"]

for ts_i, ts_v in enumerate(timestamps):
   print "Timestamp: " + str(ts_v)
   for class_i, class_v in enumerate(classes[ts_i]):
      print "Class: " + class_v + " Prob: " + str(probs[ts_i][class_i])

