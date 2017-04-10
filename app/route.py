from flask import Flask,render_template,request
import serial

app = Flask(__name__)

bluetoothSerial = serial.Serial("/dev/rfcomm1", baudrate=9600)

pins = {
        1 : {'name' : 'Light' , 'state' : False },
        2 : {'name' : 'Fan'   , 'state' : False }
       }

@app.route('/')
def index():
    templatedata = {
                   'pins' : pins
                  }
   
    return render_template('main.html', **templateData)


@app.route("/<value>/<action>")
def action(value,action):
    
   changePin = int(value)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
       if changePin == 1:
           bluetoothSerial.write(1)
        
       if changePin == 2:
           bluetoothSerial.write(3)

       message = 'Turned' + deviceName + 'ON'
           
       pins[changePin]['state'] = True
       
      # Save the status message to be passed into the template:
      
   if action == "off":
       if changePin == 1:
           bluetoothSerial.write(0)
       if changePin == 2:
           bluetoothSerial.write(2)
       message = 'Turned' + deviceName + 'OFF'
       pins[changePin]['state'] = False   

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
