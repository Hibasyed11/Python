from tkinter import *
window=Tk()
def handle_express(event):
    """Print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_express)
window.mainloop()