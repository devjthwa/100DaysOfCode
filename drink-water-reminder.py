from plyer import notification
import time

time_hour = float(input("set hours after you want to drink water"))

while True:
    time.sleep(6 * time_hour)
    notification.notify(
        title = "Drink Water",
        message = "Dev! Drink Water, live life!",
        )