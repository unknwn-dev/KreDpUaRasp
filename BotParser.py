import ParseSite
import TgBot
import importlib

#Bot api, bot key set inside script
bot = TgBot.bot

#admin id for control
admin = 624303728


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, напиши мне номер группы что-бы посмотреть актуальное расписание(взято с сайта kre.dp.ua)")


@bot.message_handler(commands=['update'])
def ResloaDAct(message):

  if(message.from_user.id != admin):
    return

  ParseSite.Update(message, bot)

@bot.message_handler(commands=['refreshModules'])
def ReloadImports(message):

  if(message.from_user.id != admin):
    return

  importlib.reload(ParseSite)
  importlib.reload(TgBot)
  ParseSite.reloadImports(message, bot)


@bot.message_handler(content_types = ["text"])
def send_lessions(message):
  ParseSite.GetLessions(message, bot)


bot.polling()
