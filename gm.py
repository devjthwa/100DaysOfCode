import time
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

askname = input("Hey! What's Your Name?")
if(hour <= 12):
    print("good morning " +askname + "!")
elif(hour > 16):
    print("good afternoon " +askname + "!")
else:
    print("good night " +askname + "!")
t = time.strftime('%H:%M:%S')
print("Time in your courtry is " + t)