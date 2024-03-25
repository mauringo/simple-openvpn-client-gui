from flask import Flask, redirect, render_template, request, session, url_for, Response

import json
import platform
import time
import subprocess
import os 
import sys

# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
import subprocess

def get_location():
    #ip =  os.popen("curl https://api64.ipify.org").read()
    ip=subprocess.run(["curl", "https://api64.ipify.org"],capture_output=True,text=True).stdout
    response=subprocess.run(["curl", "https://ipapi.co/"+ip+"/json/"],capture_output=True,text=True).stdout
    response = json.loads(response)
    location_data = {
        "ip": ip,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location())

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
app = Flask(__name__, static_url_path='')



os.chdir(dir_path)


########## serving functions

@app.route('/')
def index():
    
    return app.send_static_file('index.html')


@app.route('/mydata',methods=['GET', 'POST'])
def stream1():              

    try:
        info = get_location()
        print(info)
        info=json.dumps(info)
        return Response(info, mimetype='json')
        
    except Exception as e:
        print(e)

@app.route('/connect',methods=['GET', 'POST'])

def conn():              
  
    try:
        os.system("snapctl stop simple-openvpn-client-gui.vpn-daemon")
        os.system("snapctl start simple-openvpn-client-gui.vpn-daemon")
        info={}
        info=json.dumps(info)
        return Response(info, mimetype='json')
    except Exception as e:
        print(e)
        info={}
        info['error']=e
        info=json.dumps(info)
        return Response(info, mimetype='json')

@app.route('/disconnect',methods=['GET', 'POST'])

def disconn():              
  
    try:
        os.system("snapctl stop simple-openvpn-client-gui.vpn-daemon")
        info={}
        info=json.dumps(info)
        return Response(info, mimetype='json')
    except Exception as e:
        print(e)
        info={}
        info['error']=e
        info=json.dumps(info)
        return Response(info, mimetype='json')

@app.route('/stream')
def stream():
    def generate():
        with open('/run/snap.simple-openvpn-client-gui/vpnlogs.log') as f:
            while True:
                yield f.read()
                time.sleep(5)

    return app.response_class(generate(), mimetype='text/plain')

##server start

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = False, port=13131)
