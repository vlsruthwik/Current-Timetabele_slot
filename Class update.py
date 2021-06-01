import pandas as pd
import pyttsx3 as ts
from datetime import datetime
import threading
import os
import time
def start_teams():
    os.system('echo "%localappdata%/Microsoft/Teams/Update.exe" --processStart "Teams.exe">teamsrunner.bat')
    time.sleep(1)
    os.system("teamsrunner")

start_teams()
cur_time = datetime.now().strftime("%I:00 %p")
cur_day = datetime.now().strftime("%A")

eng = ts.init()
eng.setProperty('rate',125)

def tell(s):
    eng.say(s)
    eng.runAndWait()
def timespeak(s):
    s = s.strip('0')
    t = s[:s.index(':')]
    return t+" "+s[-2:]

tt = pd.read_csv('S:/Class time.csv')
tt = tt.set_index('week')
tt = tt.fillna('No')


if(cur_day=='Sunday' or cur_time not in ['09:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '02:00 PM', '03:00 PM','04:00 PM']):
    tell('Currently you are having No Class')
    
else:
    next_i = list(tt.loc[cur_day].index).index(cur_time)+1
    tell('Currently you are having'+tt.loc[cur_day][cur_time]+'Class')
    
    if(next_i<7):
        tell('You are having'+tt.loc[cur_day][next_i]+'Class at'+timespeak(list(tt.loc[cur_day].index)[next_i]))
    

print(tt)

