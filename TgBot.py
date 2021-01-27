import telebot

bot = ""
try:
    bot = telebot.TeleBot("1659365904:AAGioE7u7tLsIaq4lpk6aaGKGcJiGhddSs8")
except:
    print("Wrong telegram bot key")