from viewer.display import display
from controller.controller import router
import tkinter as tk

if __name__ == "__main__":
    window =  tk.Tk()
    display = display(tk,window)
    display.setup_home(router(tk,window))
    display.window.mainloop()


