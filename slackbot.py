import re
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
import requests
from requests.auth import HTTPBasicAuth
import json


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
url = 'https://apimoto.kamgray.smallhost.pl/bike.json'

try:
    response = requests.get(url, auth=HTTPBasicAuth(os.environ['AUTH_LOGIN'], os.environ['AUTH_PASS']))
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

def get_bike(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']



@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if "Show" in text and len(text) > 4:
        if BOT_ID != user_id:
            bike_name = text.split("Show ", 1)
            parameters = {
                "model": "Requested Bike"
            }
            parameters["model"] = bike_name[1]
            response = requests.get(url, auth=HTTPBasicAuth(os.environ['AUTH_LOGIN'], os.environ['AUTH_PASS']),
                                    params=parameters)
            bike = response.json()
            try:
                bike_name[1] != bike[0]['model']
            except IndexError:
                no_bike = "I'm sorry but i couldn't find motorcycle that you looking for"
                client.chat_postMessage(channel=channel_id, text=no_bike)
            else:
                bike_spec = "*Company:* " + bike[0]['company'] + "\n*Model:* " + bike[0]['model'] + "\n*Body Type:* " + bike[0]['body_type'] + "\n*Fuel Type:* " + bike[0]['fuel_type']\
                        + "\n*Engine:* " + bike[0]['engine_description'] + "\n*Fuel system:* " + bike[0]['fuel_system'] + "\n*Cooling:* " + bike[0]['cooling']\
                        + "\n*Displacement:* " + bike[0]['displacement'] + "\n*Max power:* " + bike[0]['max_power'] + "\n*Max torque:* " + bike[0]['max_torque']\
                        + "\n*Seat height:* " + bike[0]['seat_height'] + "\n*Wet weight:* " + bike[0]['wet_weight'] + "\n*Fuel tank:* " + bike[0]['fuel_tank']\
                        + "\n*Bore:* " + bike[0]['bore'] + "\n*Stroke:* " + bike[0]['stroke'] + "\n*Clutch:* " + bike[0]['clutch'] + "\n*Front brake:* " + bike[0]['front_brake']\
                        + "\n*Rear brake:* " + bike[0]['rear_brake'] + "\n*Front suspension:* " + bike[0]['front_suspension'] + "\n*Rear suspension:* " + bike[0]['rear_suspension']

                client.chat_postMessage(channel=channel_id, text=bike_spec)


if __name__ == "__main__":
    app.run(debug=True)


