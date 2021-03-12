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

    if(len(logType) > 1 and logType[1] != "All"):
        for log in Debug.ReadLogsByType(logType[1]):
            answ += log + "\n"
        pass
    else:
        for log in Debug.ReadAllLogs():
            answ += log + "\n"

    if len(answ) > 4096:
        for x in range(0, len(answ), 4096):
            bot.send_message(message.chat.id, answ[x:x+4096])
    else:
        bot.send_message(message.chat.id, answ)
