import telebot, time, logging, sys

TOKEN = '1112054330:AAGx68ug-fhaAhSAqoe4I92LWV6-j_gmWZA'
bot = telebot.TeleBot(TOKEN)
knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
    'forecast': "Forecast your city's weather",
    'qod'    : 'Your Quotes of the day'
}

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
        bot.send_message(cid, "Hai " + m.chat.first_name)
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, " + m.chat.first_name +", no need for me to scan you again!")

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

from blueprints.weather import GetForecastWeather
@bot.message_handler(commands=['forecast'])
def forecastWeather(message):
    sent = bot.send_message(message.chat.id, 'Masukkan kotamu')
    bot.register_next_step_handler(sent, forecastSent)
def forecastSent(message):
    chatid = message.chat.id
    text = message.text
    results = GetForecastWeather().get(text)
    bot.send_message(message.chat.id, results)

from blueprints.qod import QuotesOfTheDay
@bot.message_handler(commands=['qod'])
def quotesOftheDay(message):
    results = QuotesOfTheDay().get()
    bot.send_message(message.chat.id, results)

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

bot.polling()

while True: # Don't let the main Thread end.
    pass