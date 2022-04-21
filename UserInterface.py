import tkinter
from tkinter import messagebox
from tkinter import *
import sqBase

"""
Wanna populate the Listbox with the Tasks mentioned in the Database
"""
def populate():
    listbox.delete(0,END)
    for rows in sqBase.show():
        listbox.insert(END,rows[1])
"""
Add Task Functionality
"""
def add():
    if (len(addTask.get()) == 0):
        messagebox.showerror("ERROR", "No data Available\nPlease Enter Some Task")
    else:
        sqBase.insertData(addTask.get())
        addTask.delete(0,END)
        populate()    

"""
Delete Task Functionality
"""
def deleteTask(event):
    sqBase.deleteBytask(listbox.get(ANCHOR))
    populate()

main = tkinter.Tk()
main.title("Task Manager")
main.geometry("500x600")
main.resizable(False,False)
main.configure(
    background="#1d1d1d",
)

# Task Manager Label at the Top

# Label is used to implement display boxes where you can place text or images.
tkinter.Label(
    main,
    text = 'Task Manager',
    background = "#1d1d1d",
    foreground = "#eeeeee",
    font = ("Verdana 20")
).pack(pady=10)


# tkinter.Frame is used to Organize a group of widgets
addFrame = tkinter.Frame(main,bg="#1d1d1d").pack()

# Part of Frame: Task and Button
addTask = tkinter.Entry(addFrame,font=("Verdana"),background="#eeeeee")
addTask.pack(ipadx=20,ipady=5,pady=5)
# Adding a Button 
addBtn = tkinter.Button(addFrame,
                        text="Add Task",
                        command=add,
                        background='#000000',
                        foreground='#eeeeee',
                        relief='flat',
                        font=("Verdana"),
                        highlightcolor='#000000',
                        activebackground='#1d1d1d',
                        border=0,
                        activeforeground='#eeeeee')
addBtn.pack(padx=20,pady=20,ipadx=5)

# another Label
tkinter.Label(main,
              text="Your Tasks",
              background="#1d1d1d",
              foreground='#eeeeee',
              font=("Calibri",18),
).pack(pady=10)

#Another Frame 
taskFrame = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
taskFrame.pack(fill=BOTH,expand=300)

# Part of Frame: listbox and scrollBar
scrollBar = Scrollbar(taskFrame)
scrollBar.pack(side=RIGHT,fill=Y)

listbox = Listbox(
    taskFrame,
    font=("Verdana 18 bold"),
    bg="#1d1d1d",
    fg='#eeeeee',
    
    selectbackground='#eeeeee',
    selectforeground='#1d1d1d'
)
listbox.pack(fill=BOTH,expand=300)


# Calling the Populate Function
populate()

# Configuring Listbox and ScrollBar
listbox.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listbox.yview)

listbox.bind("<Double-Button-1>",deleteTask)
listbox.bind("<Delete>",deleteTask)

# Tip: Double click to Delete
tkinter.Label(
    main,
    text='TIP: Double CLick on a Task to Delete',
    background='#1d1d1d',
    foreground='#FFEB3B',
    font=("Calibri",18),
).pack(side=BOTTOM,pady=10)

# Program will run until one closes the Window
main.mainloop()
