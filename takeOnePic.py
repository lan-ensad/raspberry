import time, libcamera, datetime
from picamera2 import Picamera2, Preview

picam = Picamera2()
### Choose resolution
config = picam.create_preview_configuration(main={"size": (3280, 2464)})
config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam.configure(config)

date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

###	To Preview uncomment
#picam.start_preview(Preview.QTGL)

picam.start()
time.sleep(1)
picam.capture_file("Pictures/"+date+".jpg")

picam.close()
