from tkinter import *
import tkinter as tk
from tkinter import ttk
import pyperclip

import DocFormat as DF

root = Tk()
root.title('Homework Formatter')
frm = ttk.Frame(root, padding=10)
frm.grid()

#variables to fill
Name = tk.StringVar(root)
ClassName = tk.StringVar(root)
questions = tk.StringVar(root)
questionans = tk.StringVar(root)
homeworkTitle = tk.StringVar(root)

def copy2clip(txt):
    pyperclip.copy(txt)
    return

def openNewWindow(title=''):
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title(title)
 
    # sets the geometry of toplevel
    newWindow.geometry("600x100")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="You cannot have letters for # of questions goofy.").pack()
    Button(newWindow, text="Damn..", command=lambda:newWindow.destroy(),justify=CENTER).pack()

def submit():
    docQuestionNum = 2
    try:
        docQuestionNum = int(docQuestionNum)
    except:
        if (not isinstance(docQuestionNum, int)):
            openNewWindow()
            return
    
    print(docQuestionNum)
    docFirstName = Name.get()
    docLastName = ClassName.get()
    docHomeworkTitle = homeworkTitle.get()
    create_formatting(docFirstName, docLastName, docHomeworkTitle, docQuestionNum)
    return

def create_formatting(Name, docHomeworkTitle):
    doc = DF.DocFormat()
    doc.set_name(Name)
    doc.set_title(docHomeworkTitle)
    
    doc.buildFormat()


    print(doc)
    copy2clip(doc)
    return

if __name__ == "__main__":
    ttk.Label(frm, text="Homework Auto Formatter !!!").grid(column=0, row=0, columnspan=3)
    #ttk.Label(frm, text="This will create a document named with the convention: [yourName]_Math_57_[homeworkName]").grid(column=0, row=1, columnspan=10)
    ttk.Label(frm, text = 'Name:').grid(column=0,row=3)
    questionEntry = ttk.Entry(frm, text = "1 - 14", textvariable=Name).grid(column=1, row=3)
    ttk.Label(frm, text="Class: ").grid(column=0, row=4)
    firstNameEntry = ttk.Entry(frm, text = "John",textvariable=ClassName).grid(column=1, row=4)
    ttk.Label(frm, text="Title: ").grid(column=0, row=5)
    lastNameEntry = ttk.Entry(frm, text = "Doe", textvariable=homeworkTitle).grid(column=1, row=5)
    ttk.Label(frm, text="Homework Title: ").grid(column=0, row=6)
    homeworkTitleEntry = ttk.Entry(frm, text = "Math 57", textvariable=homeworkTitle).grid(column=1, row=6)
    ttk.Button(frm, text='Submit', command=submit).grid(column=0, row=7,pady=20)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=7, pady=20, padx=20)
    root.mainloop()

