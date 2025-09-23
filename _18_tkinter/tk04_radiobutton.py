import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def print_selection():
    # var1.set('you have selected '+var1.get())
    label.config(text='you have selected '+var1.get())

var1 = tk.StringVar()
var1.set('A')
label = tk.Label(window, text='empty', bg='yellow',width=20)
label.pack()

tk.Radiobutton(window, text='Option A',variable=var1, value='A', command=print_selection).pack()  # 将A赋值给var1
tk.Radiobutton(window, text='Option B',variable=var1, value='B', command=print_selection).pack()
tk.Radiobutton(window, text='Option C',variable=var1, value='C', command=print_selection).pack()

window.mainloop()

