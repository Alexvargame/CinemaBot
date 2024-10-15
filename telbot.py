import telebot
import json
from currency_converter import CurrencyConverter
from telebot import types

import search_film

bot=telebot.TeleBot('6201832691:AAHaMT6ZahpxWH2Q9j3fpWB9x5UGRQQbJHI')
currency=CurrencyConverter()
params={'s':'','d':'','c':'','g':'','v':'','w':'','t':'','f':''}
s_result={}

@bot.message_handler(commands=['start'])
def start(message):
    print(dir(message))
    bot.send_message(message.chat.id,f'Привет,{message.from_user.first_name}')
    print(message.message_id,message.id)
    print(message.chat.id)
    bot.send_message(message.chat.id, f'Введите название фильма')
    params['s'] = message.text
    bot.register_next_step_handler(message, get_year)

@bot.message_handler(content_type=['text'])
def get_year(message):
    global params
    bot.send_message(message.chat.id,f'Название фильма-{message.text}')
    params['s'] = message.text

    bot.send_message(message.chat.id, f'Введите год выхода')
    bot.register_next_step_handler(message, name_film)

@bot.message_handler(content_type=['text'])
def name_film(message):
    global s_result
    global params
    #bot.send_message(message.chat.id, message.message_id - 3)
   # bot.send_message(message.chat.id,message.message_id)
    bot.send_message(message.chat.id,f'Название фильма-{params["s"]}')
    bot.send_message(message.chat.id, f'Введите год выхода')
    params['d'] = 2022
    bot.send_message(message.chat.id,params['d'])
    s_result=search_film.search_film(params)
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Результаты поиска', callback_data='result')
    btn2 = types.InlineKeyboardButton('Где посмотреть', callback_data='view')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Сделайте выбор', reply_markup=markup)

def callback(call):

    if call.data=='result':
        bot.send_message(call.message.chat.id, f'Вывести результаты:')
        for key, value in s_result.items():
            bot.send_message(call.message.chat.id, f'{key}:{value}')
    else:
        pass



def summa(message):
    global amount


    try:
        amount=str(message.text.strip())
    except ValueError:
         bot.send_message(message.chat.id,'неверная формат')
         bot.register_next_step_handler(message,summa)
         return
        
    if amount>0:  
        markup=types.InlineKeyboardMarkup(row_width=2)
        btn1=types.InlineKeyboardButton('USD/EUR',callback_data='usd/eur')
        btn2=types.InlineKeyboardButton('EUR/USD',callback_data='eur/usd')
        btn3=types.InlineKeyboardButton('USD/GBP',callback_data='usd/gbp')
        btn4=types.InlineKeyboardButton('Другие значения',callback_data='else')
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,'Выберите пару валют',reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Сумма должна быть больше нуля')
        bot.register_next_step_handler(message,summa)
    
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data!='else':
        values=call.data.upper().split('/')
        res=currency.convert(amount,values[0],values[1])
        bot.send_message(call.message.chat.id,f'Полурчается: {round(res,2)}. Можете заново ввести сумму')
        bot.register_next_step_handler(call.message,summa)
    else:
        bot.send_message(call.message.chat.id,f'Введите названия валют через /')
        bot.register_next_step_handler(call.message,my_currency)

def my_currency(message):
    try:
        
        values=message.text.upper().split('/')
        res=currency.convert(amount,values[0],values[1])
        bot.send_message(message.chat.id,f'Полурчается: {round(res,2)}. Можете заново ввести сумму')
        bot.register_next_step_handler(message,summa)
    except Exception:
        bot.send_message(message.chat.id,f'Введите значения заново')
        bot.register_next_step_handler(message,my_currency)
        
    
    
        
        
bot.polling(none_stop=True)
