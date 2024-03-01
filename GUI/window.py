from tkinter import *
from tkinter import messagebox


count = 0
def click():
    global count
    count += 1
    # messagebox.showinfo(title='message box', message=f"You clicked the button {count} times") 
    print(f"You clicked the button {count} times")

def submit():
    username = entry.get() #to get enterd string in entry widget 
    print(f"Hello {username}!")
    entry.config(state=DISABLED) # to disable entry box after submit

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

def submit2():
    input = text.get("1.0". END) #to get text input in text widget 
    print(input)


window = Tk() #instantiate an insatance of a window
window.geometry('600x600')
window.title("GUI Window")
# you can't use iamge of any formate, you need to convert in PhotoImage 
icon = PhotoImage(file='GUI/python-icon.png')
photo = PhotoImage(file='GUI/python.png')
like = PhotoImage(file='GUI/like.png')

# reduce the size of images
like = like.subsample(75, 75)
photo = photo.subsample(10, 10)

window.iconphoto(True, icon)
window.config(background='#fff')

# label = text/image widget area
label = Label(window,
               text="Hello World", 
               font=('Arial', 32, 'bold'),
               fg='#00FF00',
               bg='black',
               relief=RAISED,
               bd=10,
               padx=20, pady=20,
               image=photo,
               compound='bottom',
               )
label.pack() #or
# label.place(x=0, y=0)

# button = event handle widgets area
button = Button(window, text='Like',
                command=click,
                font=("Comic-sans", 18),
                relief=RAISED, bd=6,
                fg='#00FF00', bg="black",
                padx=10,
                activebackground='black',
                activeforeground='#00FF00',
                image=like, compound="right")
button.pack()

# entry widget = textbox that accepts a single line of user input
entry = Entry(window, font=("Arial", 18),
              fg='#00FF00', bg="black",
              show='*')
# show='char' -> show certain character in place of text in entery widget, useful when user entering password

# entry.insert(0, "Good Day ") # insert default text in entry box at 0 index
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

# text wideget = enter multiple lines of code
text = Text(window, bg="light yellow", padx=20, pady=20,
            font=("Ink Free", 18), width=20, height=8)
text.pack()

button = Button(window, text='submit', command=submit2)
button.pack()

window.mainloop() #place window on computer screen, listen for events