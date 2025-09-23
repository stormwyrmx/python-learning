import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def moveit():
    canvas.move(rectangle, 0, 2)
    canvas.move(image, 2, 0)

canvas = tk.Canvas(window, bg='blue', height=100, width=200)

photo_image = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(100, 50, anchor='nw', image=photo_image)

button = tk.Button(window, text='move', command=moveit)
button.pack()

rectangle = canvas.create_rectangle(10, 10, 40, 30)

canvas.pack()
window.mainloop()
