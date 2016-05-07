# SecuriCam

An all software security camera. Well, all software assuming you have some old hardware lying around ;)

Uses [Ziggeo](http://ziggeo.com), [Clarifai](http://clarifai.com) and [Twilio](http://twilio.com)
* Ziggeo to continuously record 10 second video clips
* These are submitted to Clarifai to look for a person
* If a person is detected a text is sent via Twilio
