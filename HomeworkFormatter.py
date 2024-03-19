import DocFormat as DF
import appui as UI
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Homework Formatter')
    app=UI.Application(master=root)
    name = app.get_name()
    title = app.get_homeworkTitle()
    className = app.get_className()
    lab = app.islab()
    questions = app.get_questions()


    doc = DF.DocFormat(name, title, className, lab, questions)
    doc.buildFormat()
    print(doc)
    app.mainloop()