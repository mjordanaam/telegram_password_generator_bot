import os
import telebot
from dotenv import load_dotenv
from functions import *

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


def lower_handler(message):
	write_file('True' if message.text == 'y' else 'False')
	text = "Lowercase letters? (y/n)\n"
	sent_msg = bot.send_message(message.from_user.id, text, parse_mode="Markdown")
	bot.register_next_step_handler(sent_msg, number_handler)


def number_handler(message):
	write_file('True' if message.text == 'y' else 'False')
	text = "Numbers? (y/n)\n"
	sent_msg = bot.send_message(message.from_user.id, text, parse_mode="Markdown")
	bot.register_next_step_handler(sent_msg, special_handler)


def special_handler(message):
	write_file('True' if message.text == 'y' else 'False')
	text = "Special characters? (y/n)\n"
	sent_msg = bot.send_message(message.from_user.id, text, parse_mode="Markdown")
	bot.register_next_step_handler(sent_msg, generate_password_and_send)


def generate_password_and_send(message):
	write_file('True' if message.text == 'y' else 'False')
	options = read_file()
	if options:
		length = int(options[0][:-1])
		uppercase = True if options[1][:-1] == 'True' else False
		lowercase = True if options[2][:-1] == 'True' else False
		numbers = True if options[3][:-1] == 'True' else False
		special = True if options[4][:-1] == 'True' else False
		password = generate_password(length, uppercase, lowercase, numbers, special)
		text = (
			"***Your password is:***\n\n"
			f"```{password}```"
		)
		bot.send_message(message.from_user.id, text, parse_mode='Markdown')
		bot.send_message(message.from_user.id, "Have a nice day!", parse_mode='Markdown')
		clear_file()
	else:
		text = "No configuration file found. Please use /generate command first."
		bot.send_message(message.from_user.id, text, parse_mode='Markdown')


def length_handler(message):
	write_file(message.text)
	text = "Uppercase letters? (y/n)\n"
	sent_msg = bot.send_message(message.from_user.id, text, parse_mode="Markdown")
	bot.register_next_step_handler(sent_msg, lower_handler)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello World!")


@bot.message_handler(commands=['generate'])
def send_welcome2(message):
	text = "PLEASE ENTER PASSWORD LENGTH"
	sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
	bot.register_next_step_handler(sent_msg, length_handler)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
	bot.send_message(message.chat.id, "Hello World!")


bot.infinity_polling()
