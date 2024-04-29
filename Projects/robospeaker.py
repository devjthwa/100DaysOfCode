import os
import win32com.client as wincom

if __name__ == '__main__':
  speak = wincom.Dispatch("SAPI.SpVoice")
  print("Welcome to RoboSpeaker 1.1 created by Dev")
  welcome = "Welcome to RoboSpeaker 1.1 created by Dev"
  speak.Speak(welcome)
  while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
      speak.Speak("Thank you! Visit again.")
      break
    command = f"{speak.Speak({x})}"
    