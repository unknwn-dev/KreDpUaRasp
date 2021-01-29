from os import write
import json
import Debug
import ParseSite
import traceback


Subs = {int() : int()}

#Db file name
subsFileName = "subs.db"

#Try open log file
try:
    subsFile = open(subsFileName, "r")
    Subs = json.load(subsFileName)
except:
    print("LoadSubsFileError " + traceback.format_exc())
    open(subsFileName, "w+")
    subsFile = open(subsFileName, "+w")


#Get user and write in db
def SubscribeUser(message, bot):
    splitMsg = message.text.split(" ")
    if not splitMsg[1] in ParseSite.lessions:
        answ = "Группа не найдена"
        bot.reply_to(message,answ)
        return
    subsFile = open(subsFileName, "+w")
    Subs[message.from_user.id] = splitMsg[1]
    subsFile.write(json.dumps(Subs))
    Debug.Log("User subscribed " + message.from_user.first_name + " on " + splitMsg[1])
    answ = "Вы подписались на рассылку расписания для групы " + splitMsg[1]
    bot.reply_to(message,answ)
