#TITLE: Source code of a Stopwatch on python script
#Author: Adenson Samuel
#Organization: Code Lagos 5.0
#Date: 12-9-2018

########################################################################################
#                                                                                      #
#                           STOPWATCH SOURCE CODE                                      #             
#                                                                                      #
########################################################################################



#importing from gui

from tkinter import *
import tkinter.messagebox as tkMessageBox
import time

def Main():
    global root
#Defining the header for the widget
    root = Tk()
    root.title("Stopwatch")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 10) - (width / 10)
    y = (screen_height / 10) - (height / 10)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=200)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=200)
    Bottom.pack(side=BOTTOM)
    #Creating and defining the start button
    Start = Button(Bottom, text='Start', command=stopWatch.Start, width=20, height=2,font=(" sans serif", 10, "bold"), fg="white",bg="lime green") 
    Start.pack(side=LEFT)
    #Creating and defining the stop button
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width= 10, height=2,font=(" sans serif", 10, "bold"), fg="white",bg="orange")
    Stop.pack(side=LEFT)
    #Creating and defining the reset button
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width= 10, height=2,font=(" sans serif", 10, "bold"), fg="white",bg="olive")
    Reset.pack(side=LEFT)
    #Creating and defining the exit button
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=10, height=2,font=(" sans serif", 10, "bold"), fg="white",bg="orange red")
    Exit.pack(side=LEFT)
    
    Title = Label(Top, text="Stopwatch ", font=("comic sans ms", 20, "bold"),fg="maroon", bg="cadetblue" )
    Title.pack(fill=X)
    root.config(bg="cadetblue")
    root.mainloop()


class StopWatch(Frame):
# Initialize the Main Function of the Stopwatch  
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()
        
# Create the widget of the Stopwatch Timer
    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("geneva", 80), fg="maroon", bg="cadetblue")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=3, padx=3)
        
# Continously Update The Time From Counting
    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
        
# calculation to Set The Value of Time When Is Called
    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        
# Start The Stopwatch Counting When Button Start Is Clicked 
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
            
# Stop The Stopwatch Counting When Button Stop Is Clicked
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
            
# Close The Application When Exit Button Is Clicked
    def Exit(self):
        result = tkMessageBox.askquestion('Stopwatch', 'Do you want to exit Stopwatch?', icon='warning')
        if result == 'yes':
            root.destroy()
            exit()
            
# Reset The Timer When Reset Button Is Clicked
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    Main()
