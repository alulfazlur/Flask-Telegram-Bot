import telebot, time, logging, sys, requests

TOKEN = '1112054330:AAGx68ug-fhaAhSAqoe4I92LWV6-j_gmWZA'
bot = telebot.TeleBot(TOKEN)
knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'     : 'Get used to the bot',
    'help'      : 'Gives you information about the available commands',
    'umbrella'  : "Should you bring the umbrella?",
    'qod'       : 'Your quotes of the day',
    'track'      : 'Your track of the day'
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
import json
@bot.message_handler(commands=['umbrella'])
def forecastWeather(message):
    sent = bot.send_message(message.chat.id, 'Where are you now?')
    bot.register_next_step_handler(sent, forecastSent)
def forecastSent(message):
    chatid = message.chat.id
    text = message.text
    get = 'http://0.0.0.0:9000/weather?q=%s' % (text)
    req = requests.get(get)
    res = req.json()
    # weath = json.loads(req.data)
    # results = GetForecastWeather().getBot(text)
    bot.send_message(message.chat.id, 'You are in ' + text + ' now, at '+ res['date'] + '\n' + res['weather today'])

from blueprints.qod import QuotesOfTheDay
@bot.message_handler(commands=['qod'])
def quotesOftheDay(message):
    results = QuotesOfTheDay().getBot()
    bot.send_message(message.chat.id, results)

from blueprints.track import TracksOfTheDay
# @bot.message_handler(commands=['track'])
# def forecastWeather(message):
#     results = TracksOfTheDay().getBot()
#     bot.reply_to(message, results)

@bot.message_handler(commands=['all'])
def forecastWeather(message):
    sent = bot.send_message(message.chat.id, 'Where are you now?')
    bot.register_next_step_handler(sent, all)
def all(message):
    result = ''
    chatid = message.chat.id
    text = message.text

    weather_of_the_day = 'http://0.0.0.0:9000/weather?q=%s' % (text)
    req_weather = requests.get(weather_of_the_day)
    res_weather = req_weather.json()
    result += '--Weather of the day--\nYou are in ' + text + ' now, at '+ res_weather['date'] + '\n' + res_weather['weather today'] + '\n'

    quote_of_the_day = 'http://0.0.0.0:9000/qod?q=%s' % (text)
    req_quote = requests.get(quote_of_the_day)
    res_quote = req_quote.json()
    result += '\n--Quotes of the day--\n' + res_quote['quote'] + '\n-' + res_quote['author'] + '-\n'

    track_of_the_day = 'http://0.0.0.0:9000/track?q=%s' % (text)
    req_track = requests.get(track_of_the_day)
    res_track = req_track.json()
    result += '\n--Track of the day--\n' + res_track['title'] + ' - ' + res_track['singer'] + '\n' + res_track['link']

    # results = "Good morning, kawula muda!\n\n--Weather today--\n%s\n\n--Quotes of the day--\n%s\n\n--Song for you--%s" % (weather_of_the_day, quotes_of_the_day, track_of_the_day)
    bot.send_message(message.chat.id, result)

bot.polling()

while True: # Don't let the main Thread end.
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        logging.error(err)
        time.sleep(60)