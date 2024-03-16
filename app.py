from flask import Flask , render_template
from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor

camera = PiCamera()
pir = MotionSensor(4)
# i = 0 (maybe to store it in a list)

# stick function in while loop
# have integer variable that starts as 0 
# every time it record, plus 1 the variable
# use counter in vid name

def recording():
    pir.wait_for_no_motion()
    pir.wait_for_motion()
    camera.start_recording('/home/pi/Desktop/Snapshots/video.h264')
    sleep(4)
    camera.stop_recording()
    camera.close()
    # i = +1
    # pir.wait_for_no_motion()

app = Flask("__name__")


@app.route("/")
def index():
    recording()
    return render_template('index.html', 'videos')

@app.route("/test")
def hello_world2():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True, port=5040, host='0.0.0.0')

#open website from macbook next time


    
# Look for motion (done)
# recordMotion (stop looking for motion) (done)
# get most recent video (already, does it)
# maybe store it 
# play it in the website
# send to email or discard it
# repeat loop manually