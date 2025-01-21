import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')



tk.Button(window, text='hit me showinfo', command=lambda: messagebox.showinfo(title='Hi', message='hahahahah')).pack()
tk.Button(window, text='hit me show warning', command=lambda: messagebox.showwarning(title='Hi', message='nononnono')).pack()
tk.Button(window, text='hit me show error', command=lambda: messagebox.showerror(title='Hi', message='wrongwrongwrong')).pack()
tk.Button(window, text='hit me ask question',
          command=lambda: print(messagebox.askquestion(title='question', message='are you sure you wanna quit?'))).pack()
# 返回值为yes或者no
tk.Button(window, text='hit me ask okcancel',command=lambda: print(messagebox.askokcancel(title='okcancel', message='are you sure you wanna quit?'))).pack()
# 返回值为True或者False
window.mainloop()
