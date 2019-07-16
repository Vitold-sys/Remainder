import telebot
import schedule
import emoji
import requests
import random

    
owm = pyowm.OWM('Token', language="ru")

smiles = ['🤣', '😕', '😊', '😀', '😌', '👄', '👎', '👅', '👀', '😊', '🧐', '🤓', '🙃', '💍', '💩']
animals = ['🐶', '🐴', '🐗', '🦓', '🦒', '🦌', '🐢', '🐍', '🐻', '🐑', '🐖', '🐓', '🐇', '🐀', '🐒']

def telegram_bot_sendtext(bot_message):
    bot_token = 'Token'
    bot_chatID = 'Chatid'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID +\
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    my_balance = 50
    my_message = "Привет. Ты уже не пишешь мне: {} минут".format(my_balance) + random.choice(smiles)
    telegram_bot_sendtext(my_message)


def lol():
    sad = emoji.emojize(":cry:", use_aliases=True)
    my_balance = 2
    my_message = "Привет, ты там не забываешь обо мне? Ты уже не пишешь мне: {} часа".format(my_balance) + str(sad)
    telegram_bot_sendtext(my_message)


def saturday():
    love = emoji.emojize(":heart:", use_aliases=True)
    couple = emoji.emojize(":couplekiss:", use_aliases=True)
    couple1 = emoji.emojize(":couple_with_heart:", use_aliases=True)
    my_message = "Сейчас самое счастливое время по мнению ученых." + "\n" +\
                 "Если вы вместе, то быстро сказали, что любите друг друга. " + str(love) + "\n" + \
                 "Если вы не вместе, то быстро написали, что любите друг друга и послали обнимашку. " + str(couple) \
                 + str(couple1)
    telegram_bot_sendtext(my_message)


def goodnight():
    night = emoji.emojize(":sleeping:", use_aliases=True)
    my_message = "Доброй ночки" + "\n" + str(night)
    telegram_bot_sendtext(my_message)


def goodmorning():
    morning = emoji.emojize(":sunny:", use_aliases=True)
    my_message = "Доброго утречка" + "\n" + str(morning)
    telegram_bot_sendtext(my_message)


def sad():
    angry = emoji.emojize(":heart:", use_aliases=True)
    my_message = "Если вы поссорились" + str(angry) +"," + "\n" + "То Вит:" + random.choice(animals) + "\n" +\
                 "А ты, Вероника" + random.choice(animals)
    telegram_bot_sendtext(my_message)


def eat():
    eatt = emoji.emojize(":watermelon:", use_aliases=True)
    my_message = "Время покушать" + "\n" + str(eatt)
    telegram_bot_sendtext(my_message)


def pogoda():
    intro = emoji.emojize(":small_orange_diamond:", use_aliases=True)
    tempem = emoji.emojize(":sunny:", use_aliases=True)
    humem = emoji.emojize(":droplet:", use_aliases=True)
    windem = emoji.emojize(":dash:", use_aliases=True)
    minsk = owm.weather_at_place('Minsk, BY')
    w = minsk.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    wind = w.get_wind()["speed"]
    my_message = str(intro) + "В Минске сейчас: " + w.get_detailed_status() + "\n" +\
                 str(intro) + "Температура в данный момент в районе: " + str(temp) + str(tempem) + "\n" +\
                 str(intro) + "Влажность: " + str(hum) + " % " + str(humem) + "\n" + \
                 str(intro) + "Скорость ветра: " + str(wind) + " м/с " + str(windem)
    telegram_bot_sendtext(my_message)
    

schedule.every(1).minutes.do(report)
schedule.every(2).hours.do(lol)
schedule.every().saturday.at("19:30").do(saturday)
schedule.every().day.at("09:00").do(goodmorning)
schedule.every().day.at("10:30").do(sad)
schedule.every().day.at("14:30").do(sad)
schedule.every().day.at("22:30").do(goodnight)
while True:
    schedule.run_pending()
    time.sleep(1)
