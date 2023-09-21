import time, libcamera, datetime
from picamera2 import Picamera2, Preview

picam = Picamera2()
### Choose resolution
config = picam.create_preview_configuration(main={"size": (3280, 2464)})
config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam.configure(config)

###	To Preview uncomment
#picam.start_preview(Preview.QTGL)


picam.start()

for x in range(12):
	date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
	picam.capture_file("Pictures/"+date+".jpg")
	time.sleep(4.5)
	
picam.close()
