import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)  # Add padding to the sides of the window
        self.create_widgets()

    def create_widgets(self):
        self.textboxes = []
        for i in range(3):
            self.create_textbox()

        self.combo = ttk.Combobox(self.master)
        self.combo['values'] = [i for i in range(1, 11)]
        self.combo.current(0)
        self.combo.pack()
        self.combo.bind('<<ComboboxSelected>>', self.add_textboxes)

        # Add two buttons at the bottom of the window
        self.button1 = tk.Button(self.master, text="Button 1", command=self.save_values)
        self.button1.pack(side=tk.BOTTOM)
        self.button2 = tk.Button(self.master, text="Button 2")
        self.button2.pack(side=tk.BOTTOM)

    def create_textbox(self):
        textbox = tk.Text(self.master, height=1, width=40)
        textbox.pack()
        self.textboxes.append(textbox)

    def add_textboxes(self, event):
        num = int(self.combo.get())
        for i in range(num):
            self.create_textbox()

    def save_values(self):
        self.values = [textbox.get("1.0", tk.END).strip() for textbox in self.textboxes]
        print(self.values)  # Print the values to the console

    def open_error_window(self, e = "Error: ur dumb"):
        newWindow = tk.Toplevel(self.master)
        newWindow.title('Error')
        newWindow.geometry('600x100')
        tk.Label(newWindow, text=e).pack()
        tk.Button(newWindow, text='Damn..', command=lambda: newWindow.destroy(), justify=tk.CENTER).pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
