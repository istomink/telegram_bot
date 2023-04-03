import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6250260424:AAE4p3ap7oAxCGFlsg8eIHjDXATCxL_h0qI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Приветик, {message.from_user.first_name}!')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/istomink')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт'))
    bot.reply_to(message, 'Классная картинка!')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Приветик, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)