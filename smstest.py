import os
from twilio.rest import TwilioRestClient 
 
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"] 

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 
 
client.messages.create(
    to = "your mobile number", 
    from_ = "your twilio number", 
    body = "Person detected, view video http://embed.ziggeo.com/v1/applications/13234d4509cd5858e459a24e1494520d/videos/d75a98bf57a4a2c0cf225f057b545bd0/video.mp4", 
)
