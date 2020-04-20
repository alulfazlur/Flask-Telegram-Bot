import telebot, time, logging, sys

TOKEN = '1112054330:AAGx68ug-fhaAhSAqoe4I92LWV6-j_gmWZA'
bot = telebot.TeleBot(TOKEN)

# def echo_messages(messages):
#     """
#     Echoes all incoming messages of content_type 'text'.
#     """
#     for m in messages:
#         chatid = m.chat.id
#         if m.content_type == 'text':
#             text = m.text
#             bot.send_message(chatid, text)


# Handle /start and /help
@bot.message_handler(commands=['start'])
def command_help(message):
    bot.reply_to(message, "Hello, did someone call for help?")


# @bot.message_handler(commands=['help'])
# def help_command(message):
#    keyboard = telebot.types.InlineKeyboardMarkup()
#    keyboard.add(
#        telebot.types.InlineKeyboardButton(
#            ‘Message the developer’, url='telegram.me/artiomtb'
#        )
#    )
#    bot.send_message(
#        message.chat.id,
#        '1) To receive a list of available currencies press /exchange.\n' +
#        '2) Click on the currency you are interested in.\n' +
#        '3) You will receive a message containing information regarding the source and the target currencies, ' +
#        'buying rates and selling rates.\n' +
#        '4) Click “Update” to receive the current information regarding the request. ' +
#        'The bot will also show the difference between the previous and the current exchange rates.\n' +
#        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
#        reply_markup=keyboard
#    )

from blueprints.weather import GetForecastWeather
@bot.message_handler(commands=['forecast'])
def forecastWeather(message):
    results = GetForecastWeather().get()
    bot.reply_to(message, results)

from blueprints.qod import QuotesOfTheDay
@bot.message_handler(commands=['qod'])
def forecastWeather(message):
    results = QuotesOfTheDay().get()
    bot.reply_to(message, results)

from blueprints.track import TracksOfTheDay
@bot.message_handler(commands=['song'])
def forecastWeather(message):
    results = TracksOfTheDay().get()
    bot.reply_to(message, results)

@bot.message_handler(commands=['all'])
def forecastWeather(message):
    weather_of_the_day = GetForecastWeather().get()
    quotes_of_the_day = QuotesOfTheDay().get()
    track_of_the_day = TracksOfTheDay().get()
    results = "Good morning, kawula muda!\n\n--Weather today--\n%s\n\n--Quotes of the day--\n%s\n\n--Song for you--%s" % (weather_of_the_day, quotes_of_the_day, track_of_the_day)
    bot.reply_to(message, results)

# bot.set_update_listener(echo_messages)
bot.polling()

while True: # Don't let the main Thread end.
    pass