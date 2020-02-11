#This is a simple clock with three main functionalities:
#1. checking time 2. setting time 3. setting alarm
#Author: Lwazilwenkosi Mpofu
#Version: 1.0.0

import datetime

#the beep sound will work only for windows pc (for now)
import winsound

def check_time():
    alarmHour = datetime.datetime.now().hour
    alarmMinute = datetime.datetime.now().minute
    print("Time is"+str(alarmHour)+":"+str(alarmMinute))

def set_time():
    alarmHour = int(input("Enter Hour in 24 hour notation: "))
    alarmMinute = int(input("Enter Minute: "))
    new_time = datetime.time(alarmHour,alarmMinute,00)
    print(new_time)

def set_alarm():
    alarmHour = int(input("Enter Hour in 24 hour notation: "))
    alarmMinute = int(input("Enter Minute: "))
    while True:
        if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
            print("wake up!")
            
            duration = 120000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
def options():
    option = int(input("Enter 1 to see time, 2 to set time, 3 to set alarm: "))

    #When user selects 1, current time will be displayed
    if option == 1:
        check_time()
    #When user selects 2, they would be given an option to set a new time
    elif option == 2:
        set_time()
    #when user selects 3, they would be given an option to set an alarm (in future, two alarms should be set)
    elif option ==3:
        set_alarm()
    else:
        return option
        #option = int(input("Enter 1 to see time, 2 to set time, 3 to set alarm"))
    
def main():
    print("Welcome to a simple clock.\n This clock allows you to set time, check time, and set alarm")
    options()
main()
