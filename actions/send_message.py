from configs import bot_token, dev_token, dev_chat_id
import requests
import time

url_dev = "https://api.telegram.org/bot{0}/sendMessage".format(dev_token)
url = "https://api.telegram.org/bot{0}/sendMessage".format(bot_token)


def message_user(message_text, chat_id):
	message_data = {
	'chat_id': chat_id,
	'text': message_text,
	'parse_mode':'HTML'
	}
	requests.post(url, data=message_data)

def message_dev(message_text):
	message_data = {
	'chat_id': dev_chat_id,
	'text': message_text,
	'parse_mode':'HTML'
	}
	requests.post(url_dev, data=message_data)