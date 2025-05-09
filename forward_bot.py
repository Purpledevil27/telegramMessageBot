# forward_bot.py

# Importing necessary modules
import os
import logging
from telethon import TelegramClient, events
from config import api_id, api_hash
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetching channel details from environment variables
source_channel_name = int(os.getenv('SOURCE_CHANNEL', 0))  # Source channel ID
destination_channel = os.getenv('DESTINATION_CHANNEL')  # Destination channel URL or ID

# Fetching session name from environment variables (default: 'session')
session_name = os.getenv('SESSION_NAME', 'session')

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Configure logging for better error tracking and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Event handler for new messages in the source channel
@client.on(events.NewMessage(chats=source_channel_name))
async def forward_handler(event):
    message = event.message  # Extract the message object from the event

    try:
        # Forward text messages
        if message.text:
            await client.send_message(destination_channel, message.text)
        # Forward media files with optional captions
        elif message.media:
            await client.send_file(destination_channel, file=message.media, caption=message.text or '')
        else:
            # Log unhandled message types
            logger.warning(f"Unhandled message type: {message}")
    except Exception as e:
        # Log any errors that occur during message forwarding
        logger.error(f"Error forwarding message: {e}")

# Start the Telegram client
client.start()
logger.info("🚀 Forwarding bot is running...")

# Keep the bot running until manually stopped
client.run_until_disconnected()
