# config.py

import os

api_id = int(os.getenv('API_ID', 0))
api_hash = os.getenv('API_HASH', '')

SOURCE_CHANNEL = int(os.getenv('SOURCE_CHANNEL', 0))
DESTINATION_CHANNEL = os.getenv('DESTINATION_CHANNEL', '')
