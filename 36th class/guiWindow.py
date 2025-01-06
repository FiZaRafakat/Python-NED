# from tkinter import Tk , Label
# r = Tk()

# from tkinter import * # not preferable
# r = Tk()

import tkinter as tk
root = tk.Tk()

def func():
    text = tk.Label(root,text = "Hey!!! 🤗",font=("Times New Roman", 20),bg='#Ede8d0')
    text.pack()

root.title('My Window')
root.geometry('400x400+1200+0')
root.minsize(200,200)
# root.maxsize(800,800)
label = tk.Label(text = "Beautiful flower",font=("Times New Roman", 50),bg='#Ede8d0')
label.pack()
photo1 = tk.PhotoImage(file = 'flower-photo.png')
lab2 = tk.Label(root,image = photo1 , bg='#Ede8d0')
lab2.pack()
button =tk.Button(root, text = "Click it!!",command=func,font=("Times New Roman", 20),bg='#Ede8d0')
button.pack()
root.configure(bg='#Ede8d0')
root.mainloop() #event loop (runs until gui window is closed)