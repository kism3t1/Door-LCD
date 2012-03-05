import tkinter
from tkinter import *
import time
import datetime
import socket

#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(("172.18.208.19", 5000))

#print ("Connected to Server:")

the_Time = datetime.datetime.now()

class gui(tkinter.Tk):
        def __init__(self,parent):
                tkinter.Tk.__init__(self,parent)
                self.parent = parent
                self["background"] = "white"
                self.initialize()
                
        def initialize(self):
                self.grid()

                Label = tkinter.Label(self, text='LCD Displaying:  ')
                Label.grid(column=0, row=0)
                Label["background"] = "white"
                
                Label = tkinter.Label(self, text='', width=20)
                Label.grid(column=1, row=0, columnspan=2)
                Label["background"] = "white"

                
                button = tkinter.Button(self, text=("Come in"), width=10,
                                        command=self.ComeinButtonClick)
                button["background"] = "#E0EEEE"
                button.grid(column=0, row=1, padx=5, pady=5)

                button = tkinter.Button(self, text=("Face"), width=10,
                                        command=self.FaceButtonClick)
                button["background"] = "#E0EEEE"
                button.grid(column=0, row=2, padx=5, pady=5)
                
                button = tkinter.Button(self, text=("Out of Office"), width=10,
                                        command=self.OutButtonClick)
                button["background"] = "#E0EEEE"
                button.grid(column=1, row=1, pady=5)
                
                button = tkinter.Button(self, text=("In office"), width=10,
                                        command=self.InButton)
                button["background"] = "#E0EEEE"
                button.grid(column=2, row=1, padx=5)

                button = tkinter.Button(self, text=("."), width=10,
                                        command=self.AboutWindow)
                button["background"] = "#E0EEEE"
                button.grid(column=2, row=2, padx=5)

                button = tkinter.Button(self, text=("In a Meeting"), width=10,
                                        command=self.meetingButton)
                button["background"] = "#E0EEEE"
                button.grid(column=1, row=2, pady=15)

                button = tkinter.Button(self, text=("Exit!"), width=10,
                                        command=self.ExitButton)
                button["background"] = "#E0EEEE"
                button.grid(column=2, row=4, pady=10)

                button = tkinter.Button(self, text=("About"), width=10,
                                        command=self.AboutWindow)
                button["background"] = "#E0EEEE"
                button.grid(column=1, row=4, padx=10)

                button = tkinter.Button(self, text=("Close"), width=10,
                                        command=self.CloseButton)
                button["background"] = "#E0EEEE"
                button.grid(column=0, row=4, pady=10)

                Label = tkinter.Label(self, text="LCD Door Control")
                Label.grid(column=1, row=5, columnspan=1)
                Label["background"] = "white"

                Label = tkinter.Label(self, text="V1.1")
                Label.grid(column=1, row=6)
                Label["background"] = "white"
          
                Label = tkinter.Label(self, text="Kism3t (c) 2012")
                Label.grid(column=1, row=7)
                Label["background"] = "white"


        def ComeinButtonClick(self):
                client_socket.send(b"yes")
                Label = tkinter.Label(self, text='   Come in   ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
                for k in range(10, 0, -1):
                        label1 = tkinter.Label(self, text = k)
                        label1.grid(column=2, row=0)
                        label1["background"] = "white"
                        app.update()
                        time.sleep(1)
                Label = tkinter.Label(self, text='   In office   ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
                label1["text"] = " "
        def OutButtonClick(self):
                client_socket.send(b"out")
                Label = tkinter.Label(self, text='Out of Office')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
        def InButton(self):
                client_socket.send(b"in")
                Label = tkinter.Label(self, text='   In office   ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
        def meetingButton(self):
                client_socket.send(b"meeting")
                Label = tkinter.Label(self, text='   In a Meeting   ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
        def FaceButtonClick(self):
                client_socket.send(b"face")
                Label = tkinter.Label(self, text='   Face   ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
        def ExitButton(self):
                client_socket.send(b"q")
                Label = tkinter.Label(self, text='     Exit     ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
                client_socket.close()
                exit()
        def CloseButton(self):
                client_socket.send(b"close")
                Label = tkinter.Label(self, text='     Close     ')
                Label["background"] = "white"
                Label.grid(column=1, row=0)
                client_socket.close()
                exit()

        def AboutWindow(self):
                self.grid
                #create child window
                win = Toplevel()
                win["background"] = "white"
                win.title('About')
                message = "Child Window"
                #Label(win, text="Door LCD V1.0 About").pack()
                
                Label = tkinter.Label(win, text="About Door LCD V1.1 (c) Ian Hubbard 2012", width=35)
                Label["background"] = "white"
                Label.grid(column=0, row=0, columnspan=1)
                
                Label = tkinter.Label(win, text="* Created in Python 3.2 with tkinter", width=30)
                Label["background"] = "white"
                Label.grid(column=0, row=2)
                
                Label = tkinter.Label(win, text="* Connects to Raspberry Pi on port 5000", width=30)
                Label["background"] = "white"
                Label.grid(column=0, row=3)
                
                Label = tkinter.Label(win, text="* Displays text on a LCD screen via Serial", width=30)
                Label["background"] = "white"
                Label.grid(column=0, row=4)
                
                button = tkinter.Button(win, text=("Close"), width=10,
                                        command=win.destroy)
                button["background"] = "#E0EEEE"
                button.grid(column=0, row=6, columnspan=1, pady=15)

                
                
if __name__ == "__main__":
        app = gui(None)
        app.title('Door LCD V1.1')
        app.resizable(0,0)
        app.mainloop()
