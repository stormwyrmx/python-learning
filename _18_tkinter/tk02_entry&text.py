import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

entry = tk.Entry(window)
entry.pack()

def insert_point():
    var = entry.get()
    text.insert('insert',var)

def insert_end():
    var = entry.get()
    text.insert('end',var)

tk.Button(window,text='insert point',command=insert_point).pack()
tk.Button(window,text='insert end',command=insert_end).pack()
text = tk.Text(window, height=2)
text.pack()

window.mainloop()

