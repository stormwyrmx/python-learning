import tkinter as tk

on_hit=False
def hit_me():
    global on_hit
    if on_hit:
        on_hit=False
        string_var.set('')
    else:
        on_hit=True
        string_var.set('you hit me')


window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

string_var = tk.StringVar()
label = tk.Label(window, textvariable=string_var, background='green', font=('Arial', 12), width=30, height=1)
label.pack()

button = tk.Button(window, text='hit me', width=15, height=2,command=hit_me)  # 这里是传递函数对象，而不是调用函数
button.pack()

window.mainloop()

