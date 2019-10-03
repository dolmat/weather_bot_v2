import telebot
import pyowm
from telebot.types import Message
from telebot import types


omw = pyowm.OWM('7c0bb0c14f5da7b74d25f7668ef00176', language="ru")
bot = telebot.TeleBot('447794786:AAHLQdR5Qo-T3XLtgFVUllhhoJsN0n_yM7Q')

@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    bot.send_message(message.from_user.id, 'Привет! \nНапиши название любого города России, чтобы узнать там погоду :)')


@bot.message_handler(content_types=['text'])
def send_echo(message: Message):
    try:
        observation = omw.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer = "В городе " + message.text + " сейчас " + w.get_detailed_status(
        ) + "\n"
        answer += "Температура в районе " + str(round(temp)) + "\n\n"

        if temp <= 10:
            answer += "Очень холодно"
        elif 10 < temp < 20:
            answer += "Терпимо, накинь ветровку"
        else:
            answer += "Нормально, можно в футболке"

        bot.reply_to(message, answer)
    except:
        bot.reply_to(message, 'Напиши название города, а не это...')    


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    sticker_id = 'CAADAgAD9QEAArJh9gP2aVyuvJNBwBYE'
    bot.send_sticker(message.chat.id, sticker_id)


bot.polling(none_stop=True, interval=0)
