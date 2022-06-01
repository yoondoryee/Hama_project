from flask import Blueprint, Flask, jsonify, request,render_template,make_response, redirect,url_for, Response
import Adafruit_DHT
import time
from app.camera import Camera
from app.views.auth_views import login_required
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

pin = 18	
pin1 = 20
pin2 = 21
EN1 = 16
pin3 = 19
pin4 = 26
EN2 = 13

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(EN1, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(EN2, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
#sensor = adafruit_dht.DHT11(board.D18)
bp = Blueprint('data', __name__, url_prefix='/data')

@bp.route('/camera/')
@login_required
def get_camera():
	get_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return render_template("data/get_cam.html", cur_time=get_time)

def gen(camera):
   while True:
       frame = camera.get_frame()
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
@bp.route('/humid/')
@login_required
def get_data():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None :
	    print('Temp = %0.1f*C Humid = %0.1f%' % (temperature, humidity))
	#humidity = sensor.humidity
	return render_template("data/get_data.html", hum=humidity)
    
@bp.route('/video_feed')
@login_required
def video_feed():
   return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
   


def motor1():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(EN1, GPIO.HIGH)

def motor2():
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin4, GPIO.LOW)
    GPIO.output(EN2, GPIO.HIGH)

def motor1Stop():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(EN1, GPIO.LOW)
    #GPIO.cleanup()
		
def motor2Stop():
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.LOW)
    GPIO.output(EN2, GPIO.LOW)
    #GPIO.cleanup()
		   
@bp.route('/motor')
@login_required
def motorhome(): 
   return render_template("data/motor_control.html")

@bp.route('/motor', methods = ['POST'])
@login_required
def state():
    state = request.form['motor']
    
    if(state == 'motor_on'):
       motor1()
       return motorhome()
    elif(state == 'motor_off'):
       motor1Stop()  
       return motorhome()
    elif(state == 'fan_on'):     
       motor2()
       return motorhome()
    elif(state == 'fan_off'):  
       motor2Stop()
       return motorhome()
