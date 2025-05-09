# Telegram Message Bot

## Overview
This bot forwards messages from a source Telegram channel to a destination channel using the Telethon library.

## Prerequisites
- Python 3.13 or higher
- A Telegram account
- API ID and API Hash from Telegram

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/telegramMessageBot.git
   cd telegramMessageBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:
   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   SOURCE_CHANNEL=source_channel_id
   DESTINATION_CHANNEL=destination_channel_id
   ```

4. Run the bot:
   ```bash
   python forward_bot.py
   ```

## Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t telegram-bot .
   ```

2. Run the Docker container:
   ```bash
   docker run --env-file .env telegram-bot
   ```

## Deployment
This bot is configured for deployment using Fly.io. Ensure you have the `FLY_API_TOKEN` secret set in your GitHub repository settings.

## File Descriptions
- `config.py`: Handles configuration and environment variable loading.
- `forward_bot.py`: Main bot script for forwarding messages.
- `list_channels.py`: Script to list all channels the user is part of.
- `Dockerfile`: Docker configuration for containerizing the bot.
- `requirements.txt`: Lists Python dependencies.
- `.env`: Stores sensitive information like API credentials (excluded from version control).