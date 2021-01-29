import telebot
import Debug

botKey = "1659365904:AAGioE7u7tLsIaq4lpk6aaGKGcJiGhddSs8"
bot = ""

try:
    bot = telebot.TeleBot(botKey)
except:
    print("Wrong telegram bot key")


#Get logs from Debug script and send it to user
def SendLogs(message, bot):
    logType = message.text.split(" ")
    answ = "Logs:\n"

    if(logType[1] != "All"):
        for log in Debug.ReadLogsByType(logType[1]):
            answ += log + "\n"
        pass
    else:
        for log in Debug.ReadAllLogs():
            answ += log + "\n"
    bot.reply_to(message, answ)
