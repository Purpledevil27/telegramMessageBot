from telethon import TelegramClient
from config import api_id, api_hash

client = TelegramClient('session', api_id, api_hash)

async def main():
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'{dialog.name} — ID: {dialog.id}')

with client:
    client.loop.run_until_complete(main())
