# -*- coding: utf-8 -*-
import csv
import telebot
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

raspisaniye = []

data = ""
date = ""

def parse(html):
    soup = BeautifulSoup(html,'html.parser')



    predm = soup.find_all('td',id='predm')

    rowInt=0

    data = soup.find('td',id='group')
    date = data.text

    for row in soup.find_all('td',id='group')[7:]:
        global group = row.text
        pr1 = predm[rowInt].text
        pr2 = predm[rowInt+1].text
        pr3 = predm[rowInt+2].text
        pr4 = predm[rowInt+3].text
        pr5 = predm[rowInt+4].text

        raspisaniye.append (
            "|№| group: "+group+" |\n"+
            "|0| "+pr1+"|\n"+
            "|1| "+pr2+"|\n"+
            "|2| "+pr3+"|\n"+
            "|3| "+pr4+"|\n"+
            "|4| "+pr5
        )

        rowInt += 5

try:
 bot = telebot.TeleBot("1048261255:AAGzkKbwSSwRiqaww2cEOrYXB3oNejtnrV4")
except:
 print("Wrong telegram bot key")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Привет , напиши мне номер группы что-бы посмотреть актуальное расписание(взято с сайта kre.dp.ua)")

@bot.message_handler(commands=['update'])
def ResloaDAct(message):
    raspisaniye = 0
    try:
        parse(get_html("https://www.kre.dp.ua/education-process/timetable"))
    except:
        bot.reply_to(message, traceback.format_exc())
    print(str(date))


@bot.message_handler(content_types = ["text"])
def send_raspisanye(message):
  answInt = 0
  try:
    for i in range(group, 1):
	if group[i] == message.text:
		answInt = i
    else:
      exit
    answ4 = data + "\n" + str(raspisaniye[answInt-1]).replace("\'", "")
    answ3 = answ4.replace("","")
    answ2 = answ3.replace("[","")
    answ = answ2.replace("]","") + "|"
    print(message.text + " " + message.chat.first_name)
    bot.reply_to(message,answ)
  except:
    answ = "Error"
    bot.reply_to(message,answ)


bot.polling()
