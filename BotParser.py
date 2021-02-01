import ParseSite
import TgBot
import Subscribes
import importlib

#Bot api, bot key set inside script
bot = TgBot.bot

#Get lessions from site on start
ParseSite.UpdateWithoutTg()

#admin id for control
admin = 624303728


#Welcome
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  answ = "Привет, напиши мне номер группы что-бы посмотреть актуальное расписание(взято с сайта kre.dp.ua)\n\n"
  answ += "Доступные команды : \n"
  answ += "/sub <номер группы> - подписатся на рассылку раписания"
  bot.reply_to(message, answ)


#Get lessions from site
@bot.message_handler(commands=['update'])
def ResloaDAct(message):

  if(message.from_user.id != admin):
    return

  ParseSite.Update(message, bot)

#Reload imports
@bot.message_handler(commands=['refreshModules'])
def ReloadImports(message):

  if(message.from_user.id != admin):
    return

  importlib.reload(ParseSite)
  importlib.reload(TgBot)
  importlib.reload(Subscribes)
  ParseSite.reloadImports(message, bot)


#Clear logs
@bot.message_handler(commands=['logsClear'])
def ClearLog(message):
  TgBot.Debug.ClearLogs()


#TODO: Subscribe to lessions update
@bot.message_handler(commands=['sub'])
def Subscribe(message):
  Subscribes.SubscribeUser(message, bot)

@bot.message_handler(commands=['logs'])
def Subscribe(message):
  TgBot.SendLogs(message, bot)

#Get group number and find lessions for this group
@bot.message_handler(content_types = ["text"])
def send_lessions(message):
  ParseSite.GetLessions(message, bot)


bot.polling()
