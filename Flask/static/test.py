import requests
import os
import json

import subprocess


def get_location():
    #ip =  os.popen("curl https://api64.ipify.org").read()
    ip=subprocess.run(["curl", "https://api64.ipify.org"],capture_output=True,text=True).stdout
    response=subprocess.run(["curl", "https://ipapi.co/"+ip+"/json/"],capture_output=True,text=True).stdout
    print(response)
    response = json.loads(response)
    print(response)
    location_data = {
        "ip": ip,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

print(get_location())