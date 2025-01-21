import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
counter:int=1

def fuck():
    global counter
    label.config(text='fuck'+ str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
editmenu=tk.Menu(menubar,tearoff=0)
importmenu=tk.Menu(filemenu,tearoff=0)

label = tk.Label(window, text='fuck')
label.pack()

menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New',command=fuck)
filemenu.add_command(label='Open',command=fuck)
filemenu.add_command(label='Save',command=fuck)
filemenu.add_command(label='Exit',command=window.quit)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=fuck)
editmenu.add_command(label='Copy',command=fuck)
editmenu.add_command(label='Paste',command=fuck)
filemenu.add_cascade(label='Import',menu=importmenu)
importmenu.add_command(label='Submenu',command=fuck)

window.config(menu=menubar)
window.mainloop()
