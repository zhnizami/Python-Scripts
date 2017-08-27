import time

def numbers (max): # how long a program takes to complete
    time1= time.time()
    for i in range(0,max):
        print(i)
    time2=time.time()
    print(str(time2-time1))

def askTime():  # get current time and date
    time1=time.asctime()
    print("Time1: "+time1)
    time2=str(time.localtime()    )
    print("Time2: "+time2)
 
