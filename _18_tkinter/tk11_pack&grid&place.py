import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')

# tk.Label(window, text='1').grid(row=1, column=1)

tk.Label(window, text='1').place(x=100, y=100, anchor='nw')


window.mainloop()
