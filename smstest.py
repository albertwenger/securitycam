from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC4e8c087debcf6bb904516f045d4ddd1b" 
AUTH_TOKEN = "556974b0add2c093732b37f302cd722b" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to = "+19173851022", 
    from_ = "+16462332156", 
    body = "Person detected, view video http://embed.ziggeo.com/v1/applications/13234d4509cd5858e459a24e1494520d/videos/d75a98bf57a4a2c0cf225f057b545bd0/video.mp4", 
)
