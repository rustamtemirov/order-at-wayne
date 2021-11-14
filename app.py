from flask import Flask, request, jsonify
import requests
from datetime import datetime
import logging.config
import telebot, sys
import os, re
import time

from keyboard import *
from actions import *
from configs import *
from text import *
from db import *


logging.config.fileConfig(log_ini_file, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = Flask(__name__)			
bot = telebot.TeleBot(bot_token)	

kbrs = {
	"eat":catalog_eat(),
	"dress":catalog_dress()
}


@app.route("/", methods=["POST"])
def getMessage():
	r = request.get_json()										
	#logger.info(r)
	print(r)
	if r == None:
	   return "ok", 200

	if "callback_query" in r.keys():							
		chat_id = r["callback_query"]["from"]["id"]				
		data = r["callback_query"]["data"]						
		message_id = r["callback_query"]["id"]					
		username = '0'
		if "username" in r["callback_query"]["from"]:			
			username = r["callback_query"]["from"]["username"]

		if data == "back_to_main":
			bot.send_message(chat_id=chat_id, text=text_MAIN_MENU.format(username=username), parse_mode='HTML', reply_markup=main_keyboard())
			return "ok", 200
		if data == "back_to_catalog":
			bot.send_message(chat_id=chat_id, text=text_CATALOG.format(username=username), parse_mode='HTML', reply_markup=catalog())
			return "ok", 200
		if "catalog_" in data:
			add = data.split("_")
			item_tag = add[-1]
			img_shop = open("E:\OTHER STUFFS\Projects\telegram_shop_bot\images{tag}.jpg".format(tag=item_tag), "rb")
			bot.send_photo(chat_id=chat_id, photo=img_shop, reply_markup=kbrs[item_tag])
			return "ok", 200
		if data == "go_to_cart":
			bot.send_message(chat_id=chat_id, text=user_cart(chat_id), parse_mode='HTML', reply_markup=cart())
			return "ok", 200

		if "get_" in data:
			# return "ok", 200
			add = data.split("_")
			item_tag = add[1]
			item_price = add[-1]
			img_shop = open("E:\OTHER STUFFS\Projects\telegram_shop_bot\images{tag}.jpg".format(tag=item_tag), "rb")
			bot.send_photo(chat_id=chat_id, photo=img_shop, reply_markup=item_add(item_tag, item_price))
			return "ok", 200
		if "add_" in data:
			# return "ok", 200
			add = data.split("_")
			item_tag = add[1]
			item_price = add[-1]
			add_item = addItem(user=str(chat_id), item=item_tag, price=item_price)
			if add_item is False:
				bot.answer_callback_query(callback_query_id=message_id, text='Something went wrong, sorry')
				return "ok", 200
			bot.answer_callback_query(callback_query_id=message_id, text='Added to the cart')
			return "ok", 200
		if "del_" in data:
			# return "ok", 200
			add = data.split("_")
			item_tag = add[1]
			item_price = add[-1]
			del_item = delItem(user=str(chat_id), item=item_tag, price=item_price)
			if del_item is False:
				bot.answer_callback_query(callback_query_id=message_id, text='Something went wront, sorry')
				return "ok", 200
			bot.answer_callback_query(callback_query_id=message_id, text='Removed from cart')
			return "ok", 200

	if "message" in r.keys():
		chat_id = r["message"]["chat"]["id"]									
		username = 'shop user'
		if "first_name" in r["message"]["chat"]:								
			first_name = replace_symbols(r["message"]["chat"]["first_name"])
		if "username" in r["message"]["chat"]:
			username = replace_symbols(r["message"]["chat"]["username"])
		if "last_name" in r["message"]["chat"]:
			last_name = replace_symbols(r["message"]["chat"]["last_name"])
		if "text" in r["message"]:
			text_mess = r["message"]["text"]
		else:
			bot.send_message(chat_id=chat_id, text="Unknown problem", parse_mode='HTML', reply_markup=main_keyboard())
			return "ok", 200


		if text_mess == '/start':
			bot.send_message(chat_id=chat_id, text=text_START.format(username=username), parse_mode='HTML', reply_markup=main_keyboard())
			return "ok", 200

		if text_mess == '💰 Catalogue':
			bot.send_message(chat_id=chat_id, text=text_CATALOG.format(username=username), parse_mode='HTML', reply_markup=catalog())
			return "ok", 200

		if text_mess == '🎓 Cart':
			bot.send_message(chat_id=chat_id, text=user_cart(chat_id), parse_mode='HTML', reply_markup=cart())
			return "ok", 200

		if text_mess == '🤖 Contacts':
			bot.send_message(chat_id=chat_id, text=text_CONTACT, parse_mode='HTML', reply_markup=main_keyboard())
			return "ok", 200

	return "ok", 200

def user_cart(user):
	user_items = getItem(str(user))
	if user_items == False:
		text = "Your cart is empty"
	else:
		text = "Your current cart:\n\n"
		text += "<b>Total amount: {price}</b>\n\n".format(price=user_items["all_price"])
		del user_items["all_price"]
		for item in user_items:
			text += "{item} {count}".format(item=item, count=user_items[item]["count"])
	return text


def replace_symbols(text):
	update_text = re.sub(r'\W*', '', text)
	return update_text
