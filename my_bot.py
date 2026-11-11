import telebot
import requests
bot = telebot.TeleBot('9135539986:AAH7LzCmxrwqkyClgEmD3l9QRW0hawRj8Qo')

@bot.message_handler(commands=['start'])
def send_msg(message):
    bot.send_message(message.chat.id, f'Салам {message.from_user.first_name}!')


@bot.message_handler(commands=['help'])
def send_msg(message):
    bot.reply_to(message, f'Бул бот томонку нерселерди кыла алат\n'
                          f'/start -> учурашат\n'
                          f'/info -> мен жонундо маалымат\n'
                          f'/python -> пайтон жонундо маалымат\n')


@bot.message_handler(commands=['info'])
def send_msg(message):
    bot.reply_to(message, 'Nurislam tagaev age 16')


@bot.message_handler(commands=['python'])
def send_msg(message):
    bot.reply_to(message, 'Python (Пайтон или Питон) — это популярный высокоуровневый язык программирования общего назначения, созданный Гвидо ван Россумом в конце 1980-х годов.')


@bot.message_handler(func=lambda message: True)
def send_message(message):
    text = message.text.lower()
    if text == 'салам':
        bot.reply_to(message, 'Салам кандайсын?')
    elif text == 'сени ким тузгон?':
        bot.reply_to(message, 'Мени ушул адам тузгон @Nurislam_tagaev')
    elif text == 'менин атым?':
        bot.reply_to(message, f'Сенин атын {message.from_user.first_name}!')
    elif text == 'python':
        bot.reply_to(message, f'Бул жакта пайтон боюнча маалыматтар\n'
                              f'Python:https://www.w3schools.com/python/default.asp')
    elif text == 'html':
        bot.reply_to(message, f'Бул жакта html боюнча маалыматтар\n'
                              f'Html:https://www.w3schools.com/html/default.asp')
    elif text == 'css':
        bot.reply_to(message, f'Бул жакта css боюнча маалыматтар\n'
                     f'Css:https://www.w3schools.com/css/default.asp')
    elif text == 'javascript':
        bot.reply_to(message, f'Бул жакта javascript боюнча маалыматтар\n'
                     f'JavaScript:https://www.w3schools.com/js/default.asp')
    elif text == 'sql':
        bot.reply_to(message, f'Бул жакта sql боюнча маалыматтар\n'
                     f'Sql:https://www.w3schools.com/sql/default.asp')
bot.polling(none_stop = True)

