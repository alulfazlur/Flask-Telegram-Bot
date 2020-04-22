import telebot, time, logging, sys, requests, emojis
from blueprints.weather import GetForecastWeather
from blueprints.qod import QuotesOfTheDay
from blueprints.track import TracksOfTheDay
from blueprints import app
import json

TOKEN = app.config['BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)
knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'     : 'Get used to the bot',
    'help'      : 'Gives you information about the available commands',
    'umbrella'  : "Should you bring the umbrella today?",
    'qod'       : 'Your weather and quote of the day',
    'oftheday'  : 'Your weather, quote, and track of the day'
}

rain = u'\U00002614'
thunderstorm = u'\U0001F4A8'
hot = u'\U0001F525'
love = emojis.encode(':heart:')
kiss = emojis.encode(':kissing_heart:')
funny = emojis.encode(':satisfied:')
inspire = emojis.encode(':satisfied:')
notes = emojis.encode(":notes:")

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

@bot.message_handler(commands=['umbrella'])
def startForecast(message):
    sent = bot.send_message(message.chat.id, 'Where are you now?')
    bot.register_next_step_handler(sent, outForecast)
def outForecast(message):
    chatid = message.chat.id
    text = message.text

    weather_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/weather?q=%s' % (text)
    req_weather = requests.get(weather_of_the_day)
    res_weather = req_weather.json()
    if res_weather['main'] == 'thunderstorm':
        emot_weather = thunderstorm
    elif res_weather['main'] == 'hot':
        emot_weather = hot
    else :
        emot_weather = rain
    result = emot_weather + '--Weather of the day--' + emot_weather +'\nYou are in ' + text + ' now, at '+ res_weather['date'] + '\n'+ res_weather['weather today'] + '\n'
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['qod'])
def startQod(message):
    sent = bot.send_message(message.chat.id, 'Where are you now?')
    bot.register_next_step_handler(sent, outQod)
def outQod(message):
    result = ''
    chatid = message.chat.id
    text = message.text

    weather_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/weather?q=%s' % (text)
    req_weather = requests.get(weather_of_the_day)
    res_weather = req_weather.json()
    if res_weather['main'] == 'thunderstorm':
        emot_weather = thunderstorm
    elif res_weather['main'] == 'hot':
        emot_weather = hot
    else :
        emot_weather = rain
    result += emot_weather + '--Weather of the day--' + emot_weather +'\nYou are in ' + text + ' now, at '+ res_weather['date'] + '\n'+ res_weather['weather today'] + '\n'

    quote_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/qod?q=%s' % (text)
    req_quote = requests.get(quote_of_the_day)
    res_quote = req_quote.json()
    if res_quote['category'] == 'love':
        emot_qod = kiss
    elif res_quote['category'] == 'funny':
        emot_qod = funny
    else :
        emot_qod = inspire
    result += '\n' + emot_qod +'--Quotes of the day--' + emot_qod + '\n' + res_quote['quote'] + '\n-' + res_quote['author'] + '-\n'
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['oftheday'])
def startOftheDay(message):
    sent = bot.send_message(message.chat.id, 'Where are you now?')
    bot.register_next_step_handler(sent, outOftheDay)
def outOftheDay(message):
    result = ''
    chatid = message.chat.id
    text = message.text

    weather_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/weather?q=%s' % (text)
    req_weather = requests.get(weather_of_the_day)
    res_weather = req_weather.json()
    if res_weather['main'] == 'thunderstorm':
        emot_weather = thunderstorm
    elif res_weather['main'] == 'hot':
        emot_weather = hot
    else :
        emot_weather = rain
    result += emot_weather + '--Weather of the day--' + emot_weather +'\nYou are in ' + text + ' now, at '+ res_weather['date'] + '\n'+ res_weather['weather today'] + '\n'

    quote_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/qod?q=%s' % (text)
    req_quote = requests.get(quote_of_the_day)
    res_quote = req_quote.json()
    if res_quote['category'] == 'love':
        emot_qod = kiss
    elif res_quote['category'] == 'funny':
        emot_qod = funny
    else :
        emot_qod = inspire
    result += '\n' + emot_qod +'--Quotes of the day--' + emot_qod + '\n' + res_quote['quote'] + '\n-' + res_quote['author'] + '-\n'

    track_of_the_day = 'http://0.0.0.0:'+ str(app.config['APP_PORT']) +'/track?q=%s' % (text)
    req_track = requests.get(track_of_the_day)
    res_track = req_track.json()
    result += '\n' + notes + '--Track of the day--' + notes + '\n' + res_track['title'] + ' - ' + res_track['singer'] + '\n' + res_track['link']

    bot.send_message(message.chat.id, result)

bot.polling()

while True: # Don't let the main Thread end.
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        logging.error(err)
        time.sleep(60)