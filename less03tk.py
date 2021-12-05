from tkinter import *    
import serial
import time
import serial.tools.list_ports

ser = serial.Serial('COM3',9600)
time.sleep(1)

def readSerial():
    print("reading start")
    average = 0
    sampling = 50
    sample = 0
    data = ser.read(ser.inWaiting()) 
    lbl.configure(text=data)
    print(data)
    time.sleep(1)


def clickedR():  
      ser.write(b'1')
      time.sleep(0.05)
      readSerial()
  
def clickedG():  
      ser.write(b'2')
      time.sleep(0.05)
      readSerial()
      
def clickedB():  
      ser.write(b'3')
      time.sleep(0.05)
      readSerial()  

window = Tk()  
window.title("Robot and I")  
window.geometry('640x480')  

lbl = Label(window, text="Python app for COM port", font=("Arial Bold", 16))  
lbl.place(x=80, y=50)

btnR = Button(window, text=" Red ",background="red", foreground="black",
             padx="20", pady="8", font="16", command=clickedR)  
btnR.grid(column=1, row=2)

btnG = Button(window, text="Green",background="green", foreground="black",
             padx="20", pady="8", font="16",  command=clickedG)  
btnG.grid(column=2, row=2)

btnB = Button(window, text="Blue", background="blue", foreground="black",
             padx="20", pady="8", font="16", command=clickedB)  
btnB.grid(column=3, row=2)  
 
window.mainloop()
