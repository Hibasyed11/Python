import tkinter as tk
window=tk.Tk()
window.title("Number Pad")
nums=[[1,2,3], [4,5,6], [7,8,9], ['#', 0, '*']]
for i in range(4):
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(0,3):
        window.columnconfigure(j, weight=1, minsize=75)
        frame=tk.Frame(master=window, relief='sunken', borderwidth=1)
        frame.grid(row=i, column=j)
        label=tk.Label(master=frame, text=nums[i][j], bg='#D0EFFF')
        label.pack(padx=3, pady=3)
window.mainloop()