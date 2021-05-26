from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry('1255x944')
image = Image.open('Photo from Jayavant Daware.jpg')
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()


root.mainloop()
