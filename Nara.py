from tkinter import ttk
from tkinter import *
from playsound import playsound

import time

class App:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Nara')


        #Frames
        frameSet = LabelFrame(self.wind, text="Set Time")
        frameSet.grid(column=0, row=0)

        frameTime = LabelFrame(self.wind, text = 'Time')
        frameTime.grid(column=0, row=1)
        
        #Labels

        #SetTime
        self.minutesWorking = Entry(frameSet)
        self.minutesWorking.grid(column=1, row=0)
        self.minutesBreaking = Entry(frameSet)
        self.minutesBreaking.grid(column=1, row=1)
        Label(frameSet, text='Trabajo/Minutos').grid(column=0, row=0)
        Label(frameSet, text='Descanso/Minutos').grid(column=0, row=1)

        ttk.Button(frameSet, text="Guardar cambios", command=self.SetTime).grid(row=3, column=0)

        #Time
        Label(frameTime, text="Cronómetro", font=("Arial", 32)).grid(column=0, row=0)
        self.labelTypeTime = Label(frameTime, text=" ", font=("Arial", 24))
        self.labelTypeTime.grid(row=1, column=0)
        self.counter = Label(frameTime, text="0:0", font=("Arial", 64))
        self.counter.grid(row=2, column=0, columnspan=3, pady=20)
        self.buttonChronometer = Button(frameTime, text="Empezar", command=self.StartStop)
        self.buttonChronometer.grid(row=4, column=0)
        self.buttonNext = Button(frameTime, text="Siguiente", command=self.NextChronometer)
        self.buttonNext.grid(row=5, column=0)

        #Variables
        self.chronometer = 0.0

        self.startChronometer = False

        self.typeChronometer = 0
        
        self.timeToWorking = 0.0
        self.timeToBreaking = 0.0

        self.starttime = time.time()
        self.endtime = int(self.starttime + self.chronometer * 60)

        #Sound
        self.nameAlarm = "AlarmNara.wav"

    def UpdateClock(self):        
        if self.startChronometer == True:
            now = int(time.time())

            if now <= self.endtime:
                difference = self.endtime - now
                minutes = str(difference // 60)
                seconds = str((difference % 60) // 1)
                self.counter.configure(text=str(minutes + ":" + seconds))
                print("A")
            
            if now >= self.endtime:
                playsound(self.nameAlarm)

            self.wind.after(1000, self.UpdateClock)


    def SetTime(self):
        try:
            self.timeToWorking = float(self.minutesWorking.get())
            self.timeToBreaking = float(self.minutesBreaking.get())
            self.timeToDelay = float(self.secondsDelay.get())
        except:
            print("Error, maldita sea pon números")

    def SetChronometer(self):

        self.starttime = time.time()

        if self.typeChronometer == 0:
            self.labelTypeTime.configure(text="Trabajo")
            self.chronometer = self.timeToWorking
            self.endtime = int(self.starttime + self.chronometer * 60)
        elif self.typeChronometer == 1:
            self.labelTypeTime.configure(text="Descanso")
            self.chronometer = self.timeToBreaking
            self.endtime = int(self.starttime + self.chronometer * 60)

    def NextChronometer(self):

        self.typeChronometer += 1

        if self.typeChronometer > 1:
            self.typeChronometer = 0
        
        self.SetChronometer()
        
        print(self.typeChronometer)
    
    def StartStop(self):
        if self.startChronometer == True:#Al Detener
            self.startChronometer = False
            self.labelTypeTime.configure(text="")
            self.buttonChronometer.configure(text="Empezar")
            self.counter.configure(text=str("00" + ":" + "00"))
        else:#Al Empezar
            self.startChronometer = True
            self.typeChronometer = 0
            self.SetChronometer()
            self.UpdateClock()
            self.buttonChronometer.configure(text="Detener")

window = Tk()
aplication = App(window)
window.mainloop()