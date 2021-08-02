import pandas as pd
import pyttsx3 as ts
from datetime import datetime
import webbrowser


cur_time = datetime.now().strftime("%I:00 %p")
cur_day = datetime.now().strftime("%A")

print('Today: ',cur_day)

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
times = ['09:00 AM','10:00 AM', '11:00 AM', '12:00 PM', '02:00 PM', '03:00 PM','04:00 PM']

print()
if cur_day!='Sunday':
    today_sub = list(tt.loc[cur_day])
    for i in range(7):
        print("{} : {}".format(times[i],today_sub[i]))
if(cur_day=='Sunday' or cur_time not in times):
    tell('Currently you are having No Class')
    
else:
    sub = tt.loc[cur_day][cur_time]
    next_i = list(tt.loc[cur_day].index).index(cur_time)+1
    tell('Currently you are having'+sub+'Class')
    
    if(next_i<7):
        tell('You are having'+tt.loc[cur_day][next_i]+'Class at'+timespeak(list(tt.loc[cur_day].index)[next_i]))

print("\nPress Enter to Exit")
input()



