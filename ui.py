from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from kaliui1 import Ui_Frame
import sys
import os
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

# def Speak(Audio):
#     print("   ")
#     print(f": {Audio}")
#     engine.say(Audio)
#     print("    ")
#     engine.runAndWait()


class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    # def run(self):
        # self.Task_Gui()

    # def Task_Gui(self):
        # Main.TaskExe()

    # def takecommand(self): 
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("          ")
    #         print("Listening...")
    #         r.pause_threshold = 1
    #         audio = r.listen(source)

    #     try:
    #         print("Recognizing...")    
    #         query = r.recognize_google(audio, language='en-in')
    #         print(f"Your Command :  {query}\n")

    #     except:   
    #         return "None"
            
    #     return query.lower()
        


class Gui_Start(QFrame):


    def __init__(self):

        super().__init__()

        self.jarvis_ui = Ui_Frame()
        
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

        self.jarvis_ui.pushButton_1.clicked.connect(self.close)

    def startFunc(self):

        self.jarvis_ui.gif1 = QtGui.QMovie("C://Users//HKTech//Downloads//voice.gif")

        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.gif1)

        self.jarvis_ui.gif1.start()

        self.os = os

        self.os.startfile('D:\\projectt\\gui\\dist\\jarvis\\jarvis.exe')

        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

    def showtime(self):
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = "  " + label_time 

        self.jarvis_ui.textBrowser.setText(labbel)


Gui_App = QApplication(sys.argv)

Gui_Jarvis = Gui_Start()

Gui_Jarvis.show()

exit(Gui_App.exec_())
