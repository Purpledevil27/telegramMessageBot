# list_channels.py

# Importing necessary modules
from telethon import TelegramClient
from config import api_id, api_hash

# Initialize the Telegram client
client = TelegramClient('session', api_id, api_hash)

# Asynchronous function to list all channels the user is part of
async def main():
    # Iterate through all dialogs (chats, groups, channels)
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:  # Check if the dialog is a channel
            print(f'{dialog.name} — ID: {dialog.id}')  # Print channel name and ID

# Run the main function within the client context
with client:
    client.loop.run_until_complete(main())
