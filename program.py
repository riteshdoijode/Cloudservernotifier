import requests

telegram_bot_token = "Your telegram token"
chat_id = "Your telegram chat ID"

message = "Hi from nextcloud server"

response = requests.post(
	f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage",
	params={"chat_id":chat_id,"text":message}
)

if response.status_code == 200:
	print("Message send successfullly.")
else:
	print("Failed to send message. Status code:", response.status_code)
