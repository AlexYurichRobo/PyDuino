from tkinter import *
import tkinter.ttk as ttk
import serial.tools.list_ports
import serial
import time

sendingTimeOut = 0.1
time.sleep(sendingTimeOut)

def serialPortsConfig():
    global ser
    ser = serial.Serial(cbCom.get(), 9600, timeout=0, writeTimeout=0)
    
def serial_ports():
    return  [p.device for p in serial.tools.list_ports.comports()]
def on_select(event=None):
    # get selection from event
    print("event.widget:", event.widget.get())
    
    serialPortsConfig() 
    # or get selection directly from combobox
    print("comboboxes: ", cbCom.get())   


def readSerial():
    print("reading start")
    average = 0
    sampling = 50    
    sample = 0
    data = ser.read(ser.inWaiting()) 
    lbl.configure(text=data)
    print(data)
    time.sleep(sendingTimeOut)

def clickedR():  
      ser.write(b'1')
      time.sleep(sendingTimeOut)
      readSerial()
  
def clickedG():  
      ser.write(b'2')
      time.sleep(sendingTimeOut)
      readSerial()
      
def clickedB():  
      ser.write(b'3')
      time.sleep(sendingTimeOut)
      readSerial()  

window = Tk()  
window.title("Robot and I")  
window.geometry('640x480')
cbCom = ttk.Combobox(window, values = serial_ports())
cbCom.bind('<<ComboboxSelected>>', on_select)


lbl = Label(window, text="Python app for COM port", font=("Arial Bold", 16),
             padx="20", pady="8")  
lblC = Label(window, text="COM port", font=("Arial Bold", 16),
             padx="20", pady="8")  

btnR = Button(window, text=" Red ",background="red", foreground="black",
             padx="20", pady="8", font="16", command=clickedR)
btnG = Button(window, text="Green",background="green", foreground="black",
             padx="20", pady="8", font="16",  command=clickedG)
btnB = Button(window, text="Blue", background="blue", foreground="black",
             padx="20", pady="8", font="16", command=clickedB)


lblC.grid(column=1, row=0)
cbCom.grid(column=2, row=0)
lbl.grid(column=0, row=1, columnspan=3, rowspan=2, sticky=W+E)
btnR.grid(column=1, row=4)
btnG.grid(column=2, row=4)
btnB.grid(column=3, row=4)
 
window.mainloop()
