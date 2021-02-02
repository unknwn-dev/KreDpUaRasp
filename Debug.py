import traceback
from datetime import datetime
import json

logFileName = "Logs.log"

#Logs dictionary
Logs = {"Error" : [str()], "Log" : [str()], "Warning" : [str()]}


#Try open log file
try:
    logFile = open(logFileName, "r")
    Logs = json.load(logFile)
except:
    print("LoadLogFileError " + traceback.format_exc())
    open(logFileName, "w+")
    logFile = open(logFileName, "+w")


#Write log by type
def Log(message):
    WriteLog(message, "Log")

def LogWarn(message):
    WriteLog(message, "Warning")

def LogError(message):
    WriteLog(message, "Error")


#Write log to log file
def WriteLog(message, logType):
    logFile = open(logFileName, "+w")
    Logs = json.load(logFile)
    currentTime = datetime.now()
    Logs[logType].append("(" + logType + ")(" + currentTime.strftime("%D %H:%M:%S") + ") : " + message)
    logFile.write(json.dumps(Logs))

def ReadLogsByType(logType):
    logFile = open(logFileName, "r")
    Logs = json.load(logFile)
    result = list()
    for log in Logs[logType]:
        result.append(log)
    return result

def ReadAllLogs():
    logFile = open(logFileName, "r")
    Logs = json.load(logFile)
    result = list()
    for logType in Logs:
        for log in Logs[logType]:
            result.append(log)
    return result

def ClearLogs():
    Logs = {"Error" : [str()], "Log" : [str()], "Warning" : [str()]}
    logFile = open(logFileName, "+w")
    logFile.write(json.dumps(Logs))
