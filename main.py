import telebot
import random
from telebot import types
from config import TOKEN, COLLECTION
from game_one import game, reset_score
from game_two import guess_number
from weather import get_weather_forecast_for_today, get_weather_forecast_for_tomorrow
from currency import get_rub_kgs_exchange_rate, get_usd_kgs_exchange_rate, get_usd_rub_exchange_rate

CHAT_DATA = {}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('📄 FAQ')
    button_2 = types.KeyboardButton('💻 Menu')
    button_3 = types.KeyboardButton('🛑 Woops')
    markup.add(button_1, button_2, button_3)

    welcome_text = f'Привет, *{message.from_user.username}*!\n\n' \
                   f'*Чтобы узнать о моих функциях* можешь нажать кнопку FAQ. \n' \
                   f'*Чтобы начать работу* нажми кнопку Menu'
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == '💻 Menu':
        main_menu(message)
    elif message.text == '🔙 Main menu':
        welcome(message)
    elif message.text == '🎮 Games':
        game_menu(message)
    elif message.text == 'Rock, Paper, Scissors':
        rps_buttoms(message)
    elif message.text in ['🪨', '✂️', '📃', '🛑Stop game']:
        rps_game(message)
    elif message.text == 'Guess the number':
        gtn_buttoms(message)
    elif message.text == 'Start game':
        CHAT_DATA[message.chat.id] = {'in_game': True, 'attempt': 1, "number": random.randint(1, 10)}
        bot.send_message(message.chat.id, 'Я загадал число от 1 до 10. Попробуй угадать!')
    elif message.text.isdigit() and CHAT_DATA.get(message.chat.id, {}).get('in_game', False):
        response = guess_number(message, message.chat.id, CHAT_DATA)
        bot.send_message(message.chat.id, response)
    elif message.text == 'Stop game':
        CHAT_DATA[message.chat.id] = {'in_game': False, 'attempt': 1}
        bot.send_message(message.chat.id, 'Игра окончена')
    elif message.text == '💼 Other':
        other_menu(message)
    elif message.text == 'Прогноз погоды':
        weather_button(message)
    elif message.text == 'Прогноз на сегодня':
        forecast = get_weather_forecast_for_today()
        bot.send_message(message.chat.id, forecast)
    elif message.text == 'Прогноз на завтра':
        forecast = get_weather_forecast_for_tomorrow()
        bot.send_message(message.chat.id, forecast)
    elif message.text == 'Курс валют':
        currency_button(message)
    elif message.text == 'Рубль':
        usd_rub_rate = get_usd_rub_exchange_rate()
        rub_kgs_rate = get_rub_kgs_exchange_rate()
        bot.send_message(message.chat.id, f"Курс доллара к рублю: {usd_rub_rate}\nКурс рубля к сому: {rub_kgs_rate}")
    elif message.text == 'Сом':
        usd_kgs_rate = get_usd_kgs_exchange_rate()
        rub_kgs_rate = get_rub_kgs_exchange_rate()
        bot.send_message(message.chat.id, f"Курс доллара к сому: {usd_kgs_rate}\nКурс рубля к сому: {rub_kgs_rate}")
    elif message.text == '🛑 Woops':
        random_sticker_id = random.choice(COLLECTION)
        bot.send_sticker(message.chat.id, random_sticker_id)
    elif message.text == '📄 FAQ':
        bot.send_message(message.chat.id, 'Этот бот умеет предсказывать погоду, знает курсы валют и умеет играть в игры. Смотри на кнопки - там всё понятно!ы')

    


def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('🎮 Games')
    button_2 = types.KeyboardButton('💼 Other')
    button_3 = types.KeyboardButton('🔙 Main menu')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выбери категорию', reply_markup=markup)

def game_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Rock, Paper, Scissors')
    button_2 = types.KeyboardButton('Guess the number')
    button_3 = types.KeyboardButton('🔙 Main menu')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выбери игру', reply_markup=markup)

def rps_buttoms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('🪨')
    button_2 = types.KeyboardButton('✂️')
    button_3 = types.KeyboardButton('📃')
    button_4 = types.KeyboardButton('🛑Stop game')
    button_5 = types.KeyboardButton('🔙 Main menu')

    markup.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(message.chat.id, 'Выбери оружие!', reply_markup=markup)

def rps_game(message):
    if message.chat.type == 'private':
        if message.text == '🪨':
            result = game(1)
            bot.send_message(message.chat.id, result)
        elif message.text == '✂️':
            result = game(2)
            bot.send_message(message.chat.id, result)
        elif message.text == '📃':
            result = game (3)
            bot.send_message(message.chat.id, result)
        elif message.text == '🛑Stop game':
            result = reset_score()
            bot.send_message(message.chat.id, result)
        elif CHAT_DATA.get(message.chat.id):
            gtn_guess(message)

def gtn_buttoms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Start game')
    button_2 = types.KeyboardButton('Stop game')
    button_3 =types.KeyboardButton('🔙 Main menu')

    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Сыгрыаем?', reply_markup=markup)

def gtn_start_game(message):
    bot.send_message(message.chat.id, 'Я загадал число от 1 до 10. Попробуй угадать!')
    CHAT_DATA[message.chat.id] = {"number": random.randint(1, 10), "attempt": 0} 

def gtn_guess(message):
    if message.chat.id in CHAT_DATA:
        response = guess_number(message.text, message.chat.id)
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, начните игру, нажав кнопку "Start game"')

def other_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Прогноз погоды')
    button_2 = types.KeyboardButton('Курс валют')
    button_3 = types.KeyboardButton('🔙 Main menu')

    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Что Вас интересует?', reply_markup=markup)

def weather_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Прогноз на сегодня')
    button_2 = types.KeyboardButton('Прогноз на завтра')
    button_3 = types.KeyboardButton('🔙 Main menu')
    
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'На какой день?', reply_markup=markup)

def currency_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Рубль')
    button_2 = types.KeyboardButton('Сом')
    button_3 = types.KeyboardButton('🔙 Main menu')

    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выбери валюту?', reply_markup=markup)



bot.polling(non_stop=True)
