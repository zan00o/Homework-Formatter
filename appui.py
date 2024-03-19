import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(padx=20, pady=5, sticky='nsew')  # Add padding to the sides of the window

        self.__HomeworkTitle = tk.StringVar(self.master)
        self.__ClassName = tk.StringVar(self.master)
        self.__Name = tk.StringVar(self.master)
        #self.__questions = tk.StringVar()
        self.LabORHomework = tk.BooleanVar(self.master)

        self.questions = []

        self.rowItter = self.row_itter()
        self.rowMain = 0
        
        self.make_beginning()
        self.create_widgets()
        self.make_buttons()

    ### GETTERS
    def get_homeworkTitle(self) -> str:
        return self.__HomeworkTitle.get()
    
    def get_className(self) -> str:
        return self.__ClassName.get()
    
    def get_name(self) -> str:
        return self.__Name.get()

    def get_questions(self) -> list:
        return self.questions
    
    def islab(self):
        return self.LabORHomework.get()
    ###HELPER FUNCTIONS
    def row_itter(self, sub=False):
        i = 0
        while not sub:
            yield i
            i += 1
        while sub:
            i -= 1
            yield i

    def make_beginning(self):
        self.rowMain +=1
        ttk.Label(self.master, text=f"Homework Title").grid(row=self.rowMain, column=0, sticky='w')
        hwTitleEntry = ttk.Entry(self.master, textvariable=self.__HomeworkTitle)
        hwTitleEntry.grid(row=self.rowMain, column=1, sticky='e')

        self.rowMain +=1
        ttk.Label(self.master, text=f"Class Name").grid(row=self.rowMain, column=0, sticky='w')
        classTitleEntry = ttk.Entry(self.master, textvariable=self.__ClassName)
        classTitleEntry.grid(row=self.rowMain, column=1, sticky='e')

        self.rowMain +=1
        ttk.Label(self.master, text=f"Name").grid(row=self.rowMain, column=0, sticky='w')
        NameEntry = ttk.Entry(self.master, textvariable=self.__Name)
        NameEntry.grid(row=self.rowMain, column=1, sticky='e')

        #make a binary choice for lab or homework do so using a radio button
        self.rowMain +=1
        ttk.Label(self.master, text=f"Lab or Homework").grid(row=self.rowMain, column=0, sticky='w')
        labOrHomework = ttk.Radiobutton(self.master, text="Lab", value=True, variable=self.LabORHomework)
        labOrHomework.grid(row=self.rowMain, column=1, sticky='e')
        labOrHomework = ttk.Radiobutton(self.master, text="Homework", value=False, variable=self.LabORHomework)
        labOrHomework.grid(row=self.rowMain, column=2, sticky='e')
        


    def make_buttons(self):

        self.rowMain += 1
        self.button1 = tk.Button(self.master, text="submit", command=self.submit)
        self.button1.grid(row=self.rowMain, column=0, sticky='w')
        self.button2 = tk.Button(self.master, text="quit", command=self.master.quit)
        self.button2.grid(row=self.rowMain, column=1, sticky='e')
        
            

    def create_widgets(self):
        
        
        self.rowMain +=1
        self.combo = ttk.Combobox(self.master)
        self.combo['values'] = [i-1 for i in range(1, 11)]
        self.combo.current(0)
        self.combo.grid(row=self.rowMain, column=0, sticky='w')
        self.combo.bind('<<ComboboxSelected>>', self.curr_textboxes)
        

        # Add two buttons at the bottom of the window
        

    def curr_textboxes(self, event):

        self.questions.clear()

        n = int(self.combo.get())

        for i in range(n):
            self.rowMain += 1
            entry_var = tk.StringVar(self.master)  # Create a StringVar for each entry
            self.questions.append(entry_var)  # Append the StringVar to the questions list

            ttk.Entry(self.master, textvariable=entry_var).grid(row=self.rowMain, column=1, sticky='w')
            #self.rowMain += 1
            


    def create_textbox(self, row, column):
        textbox = tk.Text(self.master, height=1, width=40)
        textbox.grid(row=row, column=column)
        self.questions.append(textbox)

    def add_textboxes(self, event):
        num = int(self.combo.get())
        for i in range(num):
            self.create_textbox(row=i+3, column=1)

    def submit(self):
        HomeworkTitle = self.__HomeworkTitle.get()
        ClassName = self.__ClassName.get()
        Name = self.__Name.get()
        Lab = self.LabORHomework.get()
        print(HomeworkTitle, ClassName, Name, Lab)
        self.save_values()
        


    def save_values(self):
        self.values = [question.get() for question in self.questions]
        print(self.values)  # Print the values to the console

    def open_error_window(self, e="Error: you're dumb"):
        newWindow = tk.Toplevel(self.master)
        newWindow.title('Error')
        newWindow.geometry('600x100')
        tk.Label(newWindow, text=e).pack()
        tk.Button(newWindow, text='Damn..', command=lambda: newWindow.destroy(), justify=tk.CENTER).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Homework Formatter')
    app = Application(master=root)
    app.mainloop()
