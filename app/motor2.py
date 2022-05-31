from flask import Flask, request, render_template 
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
	
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

@app.route('/')
def home():
   return render_template("index.html")


@app.route('/data', methods = ['POST'])
def data():
   data = request.form['led'] 
                              

   if(data == 'on'):
      GPIO.output(ledPin, 1)
      return home()
   elif(data == 'off'):
      GPIO.output(ledPin, 0)  
      return home()
   elif(data == 'clean'):     
      GPIO.cleanup()
      return home()
   elif(data == 'Restart'):  
      try:
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(ledPin, GPIO.OUT)
         return home()
      except:
         print("error")
         return home()
