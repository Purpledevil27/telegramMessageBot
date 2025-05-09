# config.py

import os

api_id = int(os.getenv('API_ID', 0))
api_hash = os.getenv('API_HASH', '')

source_channel_name = int(os.getenv('SOURCE_CHANNEL', 0))
destination_channel = os.getenv('DESTINATION_CHANNEL', '')
