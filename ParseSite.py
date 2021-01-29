import Group
import urllib.request
from bs4 import BeautifulSoup
import traceback
import importlib
import Debug

GroupLessions = Group.GroupLessions

#Site for parse (default : https://www.kre.dp.ua/education-process/timetable)
site = "https://www.kre.dp.ua/education-process/timetable"


#Variables
lessions = {}


#Update local db
def Update(message, bot):
    try:
        parse(get_html(site))
        pass
    except:
        bot.reply_to(message, traceback.format_exc())
        Debug.LogError(traceback.format_exc())
        return
    bot.reply_to(message, "Updated")
    Debug.Log("Updating lessions")

def UpdateWithoutTg():
    try:
        parse(get_html(site))
        pass
    except:
        Debug.LogError(traceback.format_exc())
        return
    Debug.Log("Updating lessions")    


#Get html by url
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


#Parse function, parse html
def parse(html):
    soup = BeautifulSoup(html,'html.parser')

    predm = soup.find_all('td',id='predm')

    rowInt=0

    for row in soup.find_all('td',id='group')[7:]:
        group = row.text

        pr = []
        pr.append(predm[rowInt].text)
        pr.append(predm[rowInt+1].text)
        pr.append(predm[rowInt+2].text)
        pr.append(predm[rowInt+3].text)
        pr.append(predm[rowInt+4].text)

        lessions[str(group)] = GroupLessions(group, pr)

        rowInt += 5

#Get lessions for group by group number
def GetLessions(message, bot):
    mesg = message.text
    try:

        if not message.text in lessions:
            
            answ = "Группа не найдена"
            
            bot.reply_to(message,answ)
            return

        answ = "|№| Группа : " + lessions[mesg].GroupNum + "|" + "\n"

        i = 0
        for lession in lessions[mesg].Lessions:
            answ += "|" + str(i) + "| " + lession + " |" + "\n"
            i += 1
        pass
    except:
        answ = "Error GetLessions \n"
        answ += traceback.format_exc()
        Debug.LogError(answ)
        pass
    Debug.Log("GetLession for " + mesg + " by " + message.from_user.first_name )
    bot.reply_to(message,answ)

#Called when we need to reload imports
def reloadImports(message, bot):
    importlib.reload(Group)
    importlib.reload(Debug)
    GroupLessions = Group.GroupLessions
    Update(message, bot)
    Debug.Log("ReloadingImports")