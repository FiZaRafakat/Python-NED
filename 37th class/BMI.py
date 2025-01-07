import tkinter as tk
root = tk.Tk()

# function
def BMI():    
    height = int(entryHeight.get())
    weight = int(entryWeight.get())
    bmi = (weight * 703)/ height**2
    L = tk.Label(root, text = "Your BMI is " + str(bmi),font=("Times New Roman", 20),bg='#ffa5ab' ,fg="#582630")
    L.pack(pady=10)


root.title('My BMI')
root.geometry('500x400+1100+0')
root.minsize(400,400)
# Welcome
label = tk.Label(text = "Welcome To BMI calculator",font=("Rubik Vinyl", 50),bg='#ffa5ab',fg="#590d22")
label.pack()
# entry for height 
labelHeight = tk.Label(root, text = "Enter your Height (inches) :",font=("Times New Roman", 20),padx = 5, pady = 10,bg='#ffa5ab',fg="#582630")
labelHeight.pack()
entryHeight = tk.Entry(root ,font=("Times New Roman", 20), width=25,bg="#ffe5d9",fg="#582630")
entryHeight.pack()
# entry for weight
labelWeight = tk.Label(root, text = "Enter your Weight (pounds) :",font=("Times New Roman", 20),padx = 5, pady = 10,bg='#ffa5ab',fg="#582630")
labelWeight.pack()
entryWeight = tk.Entry(root,font=("Times New Roman", 20), width=25,bg="#ffe5d9",fg="#582630")
entryWeight.pack()
# button 
button = tk.Button(root , text="Calculate BMI!!",command=BMI,font=("Playfair Display Italic", 20), relief='raised',bg="#ffe5d9",fg="#582630")
button.pack(pady=10)
# bg-color
root.configure(bg='#ffa5ab')
root.mainloop() #event loop (runs until gui window is closed)


