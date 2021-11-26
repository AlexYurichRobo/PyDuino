from tkinter import *    
import serial
import time

ser = serial.Serial('COM5',9600)
time.sleep(1)

def clickedR():  
      ser.write(b'1')
  
def clickedG():  
      ser.write(b'2')
def clickedB():  
      ser.write(b'3')
  

window = Tk()  
window.title("Robot and I")  
window.geometry('640x480')  

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
