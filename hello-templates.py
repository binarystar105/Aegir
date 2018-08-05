from flask import Flask, render_template, request, jsonify
import time
import datetime

#===============================================

# import urllib.request
# import time
# import json
# import RPi.GPIO as GPIO

# RPi GPIO pins used
# temp_pin = 22
# pH_pin = 23
# DOx_pin = 24

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(temp_pin,GPIO.OUT)
# GPIO.setup(pH_pin,GPIO.OUT)
# GPIO.setup(DOx_pin,GPIO.OUT)

# GPIO.output(temp_pin,GPIO.LOW)
# GPIO.output(pH_pin,GPIO.LOW)
# GPIO.output(DOx_pin,GPIO.LOW)

#===============================================

app = Flask(__name__)

counter = 0

@app.route("/")
def serve_webpage():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'ETI',
      'time': timeString,
      'PH_val': 0.00,
      'DO_val': 0.00,
      'TMP_val': 0.00
      }
   return render_template('index.html', **templateData)

@app.route("/api/PH", methods=['POST'])
def update_PH_thresholds():
   status = False      

   PH_low = request.form.get('PH_low')
   PH_high = request.form.get('PH_high')

   if PH_low and PH_high:
      status = True         
      print("Both PH contain a value")
      PH_low = float(PH_low)
      PH_high = float(PH_high)

      # [r_ts, r_temp, r_ph, r_dox] = get_sensor_vals()

      # if PH_low <= r_ph =< PH_high:
      #    print('pH relay is ON')
      #    GPIO.output(pH_pin,GPIO.HIGH)
      # else:
      #    print('Temp relay OFF')
      #    GPIO.output(pH_pin,GPIO.LOW)
   
   print(PH_low, PH_high)

   return jsonify(status)

@app.route("/api/DO", methods=['POST'])
def update_DO_thresholds():
   status = False

   DO_low = request.form.get('DO_low')
   DO_high = request.form.get('DO_high')

   if DO_low and DO_high:
      status = True
      print("Both DO contain a value")
      DO_low = float(DO_low)
      DO_high = float(DO_high)

      # [r_ts, r_temp, r_ph, r_dox] = get_sensor_vals()

      # if DO_low <= r_dox =< DO_high:
      #    GPIO.output(DOx_pin,GPIO.HIGH)
      #    print('DOx relay is ON')
      # else:
      #    print('DOx relay is OFF')
      #    GPIO.output(DOx_pin,GPIO.LOW)
   
   print(DO_low, DO_high)

   return jsonify(status)   

@app.route("/api/TMP", methods=['POST'])
def update_TMP_thresholds():
   status = False

   TMP_low = request.form.get('TMP_low')
   TMP_high = request.form.get('TMP_high')

   if TMP_low and TMP_high:
      status = True   
      print("Both TMP contain a value")
      TMP_low = float(TMP_low)
      TMP_high = float(TMP_high)

      # [r_ts, r_temp, r_ph, r_dox] = get_sensor_vals()

      # if TMP_low <= r_tmp =< TMP_high:
      #    print('Temp relay if ON')
      #    GPIO.output(temp_pin,GPIO.HIGH)
      # else:
      #    print('Temp relay OFF')
      #    GPIO.output(temp_pin,GPIO.LOW)

   print(TMP_low, TMP_high)

   return jsonify(status) 

@app.route("/api/cur_vals", methods=['POST'])
def update_curr_vals():
   # [r_ts, r_temp, r_ph, r_dox] = get_sensor_vals()
   # return jsonify({
   #    "TMP_cur_val": r_temp,
   #    "PH_cur_val": r_ph,
   #    "DO_cur_val": r_dox
   #    })   

   global counter
   counter += 1
   return jsonify({
      "TMP_cur_val": counter,
      "PH_cur_val": counter,
      "DO_cur_val": counter
      })   

# def get_sensor_vals():
#    with urllib.request.urlopen('http://192.168.137.88/info/gettraffic/1/') as response:
#       data = response.read().rstrip().decode('UTF-8')
#       _data = eval(data)
#       r_ts, r_temp, r_ph, r_dox = [_data[0][0] , _data[1][0], _data[2][0], _data[3][0]]
#       return [r_ts, r_temp, r_ph, r_dox]


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/api/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    print 'Server shutting down...'
    # GPIO.cleanup() # this ensures a clean exit  
    return jsonify(True) 


if __name__ == "__main__":
   app.run(host='0.0.0.0')
