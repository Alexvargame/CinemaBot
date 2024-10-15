
import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot=telebot.TeleBot('6201832691:AAHaMT6ZahpxWH2Q9j3fpWB9x5UGRQQbJHI')
currency=CurrencyConverter()
amount=0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'Привет,введите сумму')
    bot.register_next_step_handler(message,summa)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
