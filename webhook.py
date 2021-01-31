import json
import os
import requests

from flask import flask
from flask import request
from flask import make_response

#flask should start in gloabal layout

app =Flask(__name__)
@aap.route('/webhook', methods['POST'])

def webhook():
    req = request.get_json(silent=True , force =True)
    print (json.dumps(req, indent=4))
    res =makeResponse(req)
    r.header['Content-Type'] = "application.json"
    return r 

def makeResponse():
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=da6542de21921c1d5087b65cba62c9e0")
    json_object= r.json()
    weather = json_object['list']
    for i in range(0,30):
        if date in weather[i]['dt_txt'];
        condition = weather[i]['weather'][0]['description']
        break
        
    speech = "The forecast for" +city+ "for " +date+ "is" +condition
    return{
        "speech":speech
        "displayText": speech
        "source":"dialogflow-weather-webhook"
    }
if __name__ = '__main__':
    port = int(os.getenv('PORT',5000))
    print("starting app on on port %d", %port)
    app.run(debug=False,port=port,host='0.0.0.0')
