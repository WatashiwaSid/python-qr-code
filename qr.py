import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

win = Tk()

win.title("Siddhant's QR Maker")
win.config(background="#fed304")

def qr_code():
    text = entry1.get()
    qr = pyqrcode.create(text)
    file_name = "my qrcode"
    save_path = r"C:\Users\Lenovo\Desktop\ "
    name = save_path+file_name+' .png'
    qr.png(name, scale=10)
    image = Image.open(name)
    image = image.resize((400,400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo = image


text = ttk.Label(win,text = "Enter Your URL : ")    
text.grid(row = 0, column = 0, padx = 3, pady = 3)

entry1 = ttk.Entry(win, width = 40)
entry1.grid(row = 0, column = 1, padx = 3, pady = 3)

button = ttk.Button(win, text = "Generate", command=qr_code)
button.grid(row = 0, column = 2, padx = 3, pady = 3)

show_qr = ttk.Label(win, text = "QR Code: ")
show_qr.grid(row =1, column = 0, padx = 3, pady = 3)

win.imagelabel = ttk.Label(win, background = '#fed304')
win.imagelabel.grid(row = 2, column = 0, padx = 3, pady = 3, columnspan = 3)

win.mainloop()

