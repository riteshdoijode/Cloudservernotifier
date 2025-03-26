import requests
import schedule
import time

def telegram_bot_sendtext(bot_message):

#Telegram bot token and chat ID 

    bot_token = 'Telegram Chat Token'
    bot_chatID = 'Telegram Chat ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse-mode=MarkdownV2&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

def send_bot_started_message():
    telegram_bot_sendtext("Home server is on.")

telegram_bot_sendtext("Home server has started.")
schedule.every().day.at("08:00").do(send_bot_started_message)
schedule.every().day.at("20:00").do(send_bot_started_message)

while True:
    schedule.run_pending()
    time.sleep(1)
