import csv
import telebot

bot = telebot.TeleBot("1048261255:AAGzkKbwSSwRiqaww2cEOrYXB3oNejtnrV4")



with open('C:\\Users\\user\\Desktop\\project\\rasp.csv', 'r') as f:
  reader = csv.reader(f)
  raspisanye = list(reader)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет , напиши мне номер группы что-бы посмотреть актуальное расписание(взято с сайта kre.dp.ua)")

@bot.message_handler(content_types = ["text"])
def send_raspisanye(message):
  answInt = 0
  try:
    if int(message.text) == 50:
      answInt=23
    elif int(message.text) == 51:
      answInt=1
    elif int(message.text) == 52:
      answInt=3
    elif int(message.text) == 53:
      answInt=5
    elif int(message.text) == 54:
      answInt=7
    elif int(message.text) == 55:
      answInt=9
    elif int(message.text) == 56:
      answInt=9
    elif int(message.text) == 45:
      answInt=13
    elif int(message.text) == 46:
      answInt=15
    elif int(message.text) == 47:
      answInt=17
    elif int(message.text) == 48:
      answInt=19
    elif int(message.text) == 49:
      answInt=21
    elif int(message.text) == 38:
      answInt=25
    elif int(message.text) == 39:
      answInt=27
    elif int(message.text) == 41:
      answInt=29
    elif int(message.text) == 42:
      answInt=31
    elif int(message.text) == 44:
      answInt=33
    elif int(message.text) == 32:
      answInt=35
    elif int(message.text) == 33:
      answInt=37
    elif int(message.text) == 36:
      answInt=39
    elif int(message.text) == 37:
      answInt=41
    answ4 = str(raspisanye[answInt-1]).replace("\'", "")
    answ3 = answ4.replace(",","")
    answ2 = answ3.replace("[","")
    answ = answ2.replace("]","")
    bot.reply_to(message,answ)
  except:
    answ = "Error"
    bot.reply_to(message,answ)

bot.polling()