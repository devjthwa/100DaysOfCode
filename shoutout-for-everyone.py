import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak("Hello! We Value Every Person and give shoutout to everyone")

list = ["dev", "user", "user1", "user2", "user3", "user4"]

for i in list:
    speak.Speak("Shoutout to")
    speak.Speak(i)
speak.Speak("Thank you everyone, We will see you soon")

    