import tkinter as tk
from tkmacosx import Button


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(
            self, text="Hello World", bg='lightblue', fg='yellow', borderless=1)
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", bg='red', fg='yellow', borderless=1,
                           command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
root.geometry('500x500')
root.eval('tk::PlaceWindow . center')
root.title("Subliminal GUI")
app = Application(master=root)
app.mainloop()
