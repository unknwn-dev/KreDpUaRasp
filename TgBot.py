import telebot

bot = ""
try:
    bot = telebot.TeleBot("BotKey")
except:
    print("Wrong telegram bot key")
