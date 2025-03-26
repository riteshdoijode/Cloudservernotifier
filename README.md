# Cloudservernotifier
This is a simple Python script that sends notifications from a Nextcloud server running on Oracle instances cloud infrastructure to a specified Telegram chat using a Telegram bot. It leverages the Telegram Bot API to communicate with users, providing a seamless way to receive alerts from your server directly to your Telegram app.

## Features
- Send custom messages from your server to a Telegram chat.
- Easy integration with any Python-based server or application.
- Simple and lightweight, requiring only the `requests` library.

## Prerequisites
Before using this script, ensure you have the following:
- A Telegram account.
- A Telegram Bot (created using the [BotFather](https://core.telegram.org/bots#botfather)).
- A chat ID (you can obtain this via the [Telegram API](https://core.telegram.org/method/getUpdates)).
- Python 3.x installed on your system.
- The `requests` Python library.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/NextBotAlert.git
    ```

2. Navigate to the project folder:
    ```bash
    cd NextBotAlert
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the script with your own **Telegram Bot Token** and **Chat ID** in `send_message.py`.

## Configuration

- **Telegram Bot Token**: This can be obtained by creating a bot using the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
- **Chat ID**: You can get your chat ID using the Telegram API or other tools like [@userinfobot](https://t.me/userinfobot).

Once you have the necessary information, replace the placeholder values in the script with your bot token and chat ID.

```python
telegram_bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
