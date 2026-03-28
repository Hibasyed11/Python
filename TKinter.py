import tkinter as tk
from datetime import date
window=tk.Tk()
window.title("window")
lbl=tk.Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
name_lbl=tk.Label(text="Full Name", bg="#3895D3")
name_entry=tk.Entry()
def display():
    name=name_entry.get()
    message="Welcome to the Application! \nToday's date is:"
    greet="Hello"+name+"\n"
    text_box.insert("end", greet)
    text_box.insert("end", message)
    text_box.insert("end", date.today())
btn=tk.Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")
text_box=tk.Text(height=3)
lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()
window.mainloop()