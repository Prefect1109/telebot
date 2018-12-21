# -*- coding: utf-8 -*-
import telebot
# import requests
# from config import URL
from config import token
from telebot import types
bot = telebot.TeleBot(token)
print(bot.get_me())
print("\n\t---------------Update-----------\n\t----------------!!!!-----------")
# r = requests.get(URL+'/getMe')
# print (r.json())
# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Привет))")
@bot.message_handler(commands=['Google'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Введи команду /US или /UA\n для перехода в гугл(us,ua)")
@bot.message_handler(commands=['contacts'])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свои контакты", reply_markup=keyboard)
@bot.message_handler(commands=['info'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "добро пожаловать в наш магазин)")
@bot.message_handler(commands=['CRM'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Onebox")
@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Ничего нет)")
@bot.message_handler(commands=['UA'])
def handle_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Перейти в поисковик', url="https://www.google.com.ua")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и в гугл .ua)).", reply_markup=keyboard)
@bot.message_handler(commands=['US'])
def handle_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Перейти в поисковик', url="https://www.google.com.us")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и в гугл .us)).", reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def handle_start_help(message):
    if message.text == "a":
     bot.send_message(message.chat.id, "B")
    elif message.text == "b":
     bot.send_message(message.chat.id, "C")
    else:
     bot.send_message(message.chat.id, "Выберите команду:\n/help\n/info\n/Google\n/CRM\n/contacts")
bot.polling(none_stop=True)

