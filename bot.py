# -*- coding: utf-8 -*-
import telebot
# import requests
# from config import URL
from telebot import types
token = "621522847:AAGdNWBINmSNqyaRkohncLmESmwqUAZOcF4"
bot = telebot.TeleBot(token)
print(bot.get_me())
print("\n\t---------------Update-----------\n\t----------------!!!!-----------")

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
    bot.send_message(message.chat.id, "Ну давай")
    bot.send_message(message.chat.id, "Введите сколько есть кг\t")
    x = float(input)
    bot.send_message(message.chat.id, "Введите нужное кол-во А \t")
    a = float(input("Введите нужное кол-во А \t"))
    bot.send_message(message.chat.id, "Введите коф a \n")
    a1 = float(input("Введите коф a \n"))
    bot.send_message(message.chat.id, "Введите нужное кол-во B\t")
    b = float(input("Введите нужное кол-во B\t"))
    bot.send_message(message.chat.id, "Введите коф b\n")
    b1 = float(input("Введите коф b\n"))
    bot.send_message(message.chat.id, "Введите нужное кол-во C\t")
    c = float(input("Введите нужное кол-во C\t"))
    bot.send_message(message.chat.id, "Введите коф c\n")
    c1 = float(input("Введите коф c\n"))
    Order = (a + b + c)
    result = x - Order
    Cof = (round(a * a1) + round(b * b1) + round(c * c1))
    i = 0
    if Cof <= 0 and result < 0:
        print("EROR Cof =0")
        bot.send_message(message.chat.id, "EROR Cof =0")
        exit(code=0)
    else:
        if result < 0:
            while True:
                x = x - Cof
                a = a - round(a * a1)
                b = b - round(b * b1)
                c = c - round(c * c1)
                i = i + 1
                print("x:", x)
                if x <= 0:
                    print(i)
                    break
            print("a:", a)
            print("b:", b)
            print("a:", c)
            bot.send_message(message.chat.id, "a:", a)
            bot.send_message(message.chat.id, "b:", b)
            bot.send_message(message.chat.id, "a:", c)
            exit(code=0)

        else:
            print("Вистачає на всі замовлення")
            bot.send_message(message.chat.id, "Вистачає на всі замовлення")
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
bot.polling(none_stop=True, interval=0)





