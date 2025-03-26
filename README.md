# Cloudservernotifier
This is a simple Python script that sends notifications from a online storage server running on Oracle instances cloud infrastructure to a specified Telegram chat using a Telegram bot. It leverages the Telegram Bot API to communicate with users, providing a seamless way to receive alerts from your server directly to your Telegram app. It notifies the user when the server starts and sends scheduled reminders twice a day.

## Features
- Sends a startup message when the script runs.
- Sends daily notifications at **08:00 AM** and **08:00 PM**.
- Uses the `schedule` module to manage task execution.

## Prerequisites
Make sure you have Python installed on your system. The script requires the following Python libraries:
- `requests`
- `schedule`

You can install them using:
```bash
pip install requests schedule
```
## Confirgure

Modify the following values in the script to match your telegram bot settings:
bot_token: Your Telegram bot's API token.
bot_chatID: Your Telegram chat ID.

## Useage

python script.py

## Security Notice

Do not expose your bot token and chat ID in public repositories!
If you're uploading this to GitHub, consider using enviroment variables or a configuration file to store sensitive data.
