#This is a simple clock with three main functionalities:
#1. checking time 2. setting time 3. setting alarm

import datetime
#the beep sound will work only for windows pc (for now)
import winsound

print("This is an alarm clock")
option = int(input("Enter 1 to see time, 2 to set time, 3 to set alarm"))

#When user selects 1, current time will be displayed
if option == 1:
    
    alarmHour = datetime.datetime.now().hour
    alarmMinute = datetime.datetime.now().minute
    print("Time is"+str(alarmHour)+":"+str(alarmMinute))

#When user selects 2, they would be given an option to set a new time
elif option == 2:
    alarmHour = int(input("Enter Hour in 24 hour notation"))
    alarmMinute = int(input("Enter Minute"))
    new_time = datetime.time(alarmHour,alarmMinute,00)
    print(new_time)

#when user selects 3, they would be given an option to set an alarm (in future, two alarms should be set)
elif option ==3:
    alarmHour = int(input("Enter Hour in 24 hour notation"))
    alarmMinute = int(input("Enter Minute"))
    #amPm = str(input("AM or PM"))
    #if(amPm =="PM"):
        #alarmHour = alarmHour + 12

    while True:
        if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
            print("wakey wakey!")
            
            duration = 120000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            break
            print("exited")

    


else:
    option = int(input("Enter 1 to see time, 2 to set time, 3 to set alarm"))
