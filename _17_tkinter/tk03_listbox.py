import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def print_selection():
    value = listbox.get(listbox.curselection())
    var1.set(value)

var1 = tk.StringVar()
label = tk.Label(window, textvariable=var1, bg='yellow',width=4)
label.pack()

button = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
button.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
listbox = tk.Listbox(window, listvariable=var2)
list_items=[1, 2, 3, 4]
for item in list_items:
    listbox.insert('end', item)

listbox.pack()

window.mainloop()

