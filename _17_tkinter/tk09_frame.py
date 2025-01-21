import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='on the window').pack()

frame = tk.Frame(window)
frame.pack()
frame_left = tk.Frame(frame)
frame_right = tk.Frame(frame)
frame_left.pack(side='left')
frame_right.pack(side='right')

tk.Label(frame_left, text='on the frame_left1').pack()
tk.Label(frame_left, text='on the frame_left2').pack()
tk.Label(frame_right, text='on the frame_right1').pack()

window.mainloop()
