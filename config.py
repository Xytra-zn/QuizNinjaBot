import os
import json

# Load variables from app.json
with open('app.json', 'r') as json_file:
    config_data = json.load(json_file)

API_ID = os.environ.get('API_ID') or config_data['env']['API_ID']['value']
API_HASH = os.environ.get('API_HASH') or config_data['env']['API_HASH']['value']
BOT_TOKEN = os.environ.get('BOT_TOKEN') or config_data['env']['BOT_TOKEN']['value']
MONGO_URL = os.environ.get('MONGO_URL') or config_data['env']['MONGO_URL']['value']
OWNER_ID = os.environ.get('OWNER_ID') or config_data['env']['OWNER_ID']['value']
