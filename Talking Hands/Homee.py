from  tkinter import *
import numpy as np
import cv2
import tkinter as ttk
import time
from PIL import Image,ImageTk
import videoframe
import final
from final import main
def jumptovideo():
    root.destroy()
    final.main()

root = Tk()
winWidth = 1370
winHeight = 714
root.geometry('{}x{}'.format(winWidth, winHeight))
root.resizable(width=False, height=False)
imageFile = "bg2.jpg"

image3 = ImageTk.PhotoImage(Image.open(imageFile))
panel3 =Label(root, image=image3)
panel3.pack()
panel3.place(x=0,y=0)

imageFile = "image.png"
image1 = ImageTk.PhotoImage(Image.open(imageFile))
panel1 =Label(root, image=image1)
panel1.pack(side='top')
panel1.place(x=45,y=170)

imageFile = "image1.png"
image2 = ImageTk.PhotoImage(Image.open(imageFile))
panel2 =Label(root, image=image2)
panel2.pack(side='top')
panel2.place(x=1045,y=180)

w =Label(root, text="TALKING HANDS",font=('Baskerville Black SSi',55),relief=RAISED,bg='gold',bd=5)
w.pack()
w.place(x=353,y=230)
'''self.btn_snapshot=tkinter.Button(window, text="lets get started", width=50, command=jumptovideo)
self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)'''
#redbutton=Button(font=('CONSOLAS BOLD',35),height=4,width=20,bd=10,bg='blue')

root.geometry("1800x900")

redbutton = ttk.Button(root,text = '>>> LET\'S GET STARTED >>>',command=jumptovideo,bg='orange',font=('Baskerville Black SSi',25),bd=10)
redbutton.grid(column=4, columnspan=1, padx=500, pady=400, ipadx=10, ipady=5, row=3, rowspan=1, sticky=W+E+S+N)
redbutton.place(x=400,y=500)


root.mainloop()
