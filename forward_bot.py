from telethon import TelegramClient, events
from config import api_id, api_hash, source_channel_name, destination_channel

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_name))
async def forward_handler(event):
    message = event.message

    try:
        if message.text:
            await client.send_message(destination_channel, message.text)
        elif message.media:
            await client.send_file(destination_channel, file=message.media, caption=message.text or '')
        else:
            print("Unhandled message type")
    except Exception as e:
        print(f"Error forwarding message: {e}")

client.start()
print("🚀 Forwarding bot is running...")
client.run_until_disconnected()
