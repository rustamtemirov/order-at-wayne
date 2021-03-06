from telebot import types

def main_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	btn1 = types.KeyboardButton('π° Catalogue')
	btn2 = types.KeyboardButton('π Cart')
	btn5 = types.KeyboardButton('π€ Contacts')
	markup.add(btn1)
	markup.add(btn2, btn5)
	return markup

def cart():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="Return to main",callback_data="back_to_main"),
		types.InlineKeyboardButton(text="β Proceed to checkout",callback_data="checkout")
	)
	return keyboard        

def catalog():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="Clothes",callback_data="catalog_dress"),
		types.InlineKeyboardButton(text="Groceries",callback_data="catalog_eat"),
	)
	keyboard.add(types.InlineKeyboardButton(text="β Back",callback_data="back_to_main"))
	return keyboard    

def catalog_eat():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="Apple 1ΠΊΠ³/15 bitg",callback_data="get_apple_15"),
		types.InlineKeyboardButton(text="Potatoe 1ΠΊΠ³/10 bitg",callback_data="get_potato_10"),
	)
	keyboard.add(types.InlineKeyboardButton(text="π Cart",callback_data="go_to_cart"))
	keyboard.add(types.InlineKeyboardButton(text="Back",callback_data="catalog_eat"))
	return keyboard

def catalog_dress():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="Cap 100 bitg",callback_data="get_cap_100"),
	)
	keyboard.add(types.InlineKeyboardButton(text="π Cart",callback_data="go_to_cart"))
	keyboard.add(types.InlineKeyboardButton(text="Back",callback_data="catalog_dress"))
	return keyboard

def item_add(item, price):
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="Add",callback_data="add_{item}_{price}".format(item=item, price=price)),
		types.InlineKeyboardButton(text="Remove",callback_data="del_{item}_{price}".format(item=item, price=price)),
	)
	keyboard.add(
		types.InlineKeyboardButton(text="π Cart",callback_data="go_to_cart"),
		types.InlineKeyboardButton(text="β Proceed to checkout",callback_data="checkout")
	)
	keyboard.add(types.InlineKeyboardButton(text="Back",callback_data="back_to_catalog"))
	return keyboard

def confirm_payout():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(text="β Yes",callback_data="confirm_payout_yes"),
		types.InlineKeyboardButton(text="β No",callback_data="confirm_payout_no")
	)
	return keyboard

def cancel_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('β Cancel')
	markup.add(btn1)
	return markup