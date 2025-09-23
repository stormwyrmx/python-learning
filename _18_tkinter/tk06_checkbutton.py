import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var1 = tk.IntVar()
var2 = tk.IntVar()

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only Java')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

tk.Checkbutton(window, text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection).pack()
tk.Checkbutton(window, text='Java',variable=var2,onvalue=1,offvalue=0,command=print_selection).pack()

window.mainloop()
