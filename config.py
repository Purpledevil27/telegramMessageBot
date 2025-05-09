# config.py

# Importing necessary modules
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetching API credentials from environment variables
api_id = int(os.getenv('API_ID', 0))  # Telegram API ID
api_hash = os.getenv('API_HASH', '')  # Telegram API Hash

# Fetching channel details from environment variables
source_channel_name = int(os.getenv('SOURCE_CHANNEL', 0))  # Source channel ID
destination_channel = os.getenv('DESTINATION_CHANNEL', '')  # Destination channel URL or ID
