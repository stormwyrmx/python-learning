import tkinter as tk
from tkinter import messagebox
import pickle

window = tk.Tk()
window.title("Login Example")
window.geometry("450x300")

canvas = tk.Canvas(window, width=500, height=300)
photo_image = tk.PhotoImage(file="welcome.gif")
canvas.create_image(0, 0, anchor="nw", image=photo_image)
# The anchor point determines which part of the image is placed at the given coordinates (0, 0 in this case).
canvas.pack(side='top')

var_username = tk.StringVar()
# var_username.set('example@fuck.com')
var_password = tk.StringVar()
tk.Label(window, text="Username:").place(x=50, y=150)
tk.Label(window, text="Password:").place(x=50, y=190)
tk.Entry(window,textvariable=var_username).place(x=160, y=150)
tk.Entry(window,textvariable=var_password, show="*").place(x=160, y=190)

def user_signin():
    username = var_username.get()
    password = var_password.get()
    # 用户名和密码存储在pkl文件中，先看看有没有这个文件，没有就创建一个
    try:
        with open('user_info.pkl','rb') as f:
            user_info = pickle.load(f)
    except FileNotFoundError:
        with open('user_info.pkl', 'wb') as f:
            user_info = {'admin': 'admin'}
            pickle.dump(user_info, f)
    # 判断用户名是否存在，存在就判断密码是否正确，不存在就提示是否注册
    if username in user_info.keys():
        if password == user_info[username]:
            messagebox.showinfo(title='Welcome', message='How are you? ' + username)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = messagebox.askyesno('Welcome', 'You have not signed up yet. Sign up today?')
        if is_sign_up:
            user_signup()


def user_signup():
    window_signup = tk.Toplevel(window)
    window_signup.title('Sign up window')
    window_signup.geometry('350x200')

    def signin():
        new_username = var_new_username.get()
        new_password = var_new_password.get()
        confirm_password = var_confirm_password.get()
        with open('user_info.pkl', 'rb') as f:
            user_info = pickle.load(f)
        if new_password != confirm_password:
            messagebox.showerror('Error', 'Password and confirm password must be the same.')
        elif new_username in user_info.keys():
            messagebox.showerror('Error', 'This username has been signed up, please choose another one.')
        else:
            # 从pkl文件中读取用户信息，添加新用户信息，再写入pkl文件
            user_info[new_username] = new_password
            with open('user_info.pkl', 'wb') as f:
                pickle.dump(user_info, f)
            messagebox.showinfo('Welcome', 'Sign up successfully!')
            window_signup.destroy()

    var_new_username = tk.StringVar()
    var_new_password = tk.StringVar()
    var_confirm_password = tk.StringVar()
    tk.Label(window_signup, text='Username:').place(x=10, y=10)
    tk.Entry(window_signup, textvariable=var_new_username).place(x=150, y=10)
    tk.Label(window_signup, text='Password:').place(x=10, y=50)
    tk.Entry(window_signup, textvariable=var_new_password, show='*').place(x=150, y=50)
    tk.Label(window_signup, text='Confirm password:').place(x=10, y=90)
    tk.Entry(window_signup, textvariable=var_confirm_password, show='*').place(x=150, y=90)

    tk.Button(window_signup, text='Sign up', command=signin).place(x=150, y=130)


tk.Button(window, text="Sign in", command=user_signin).place(x=170,y=230)
tk.Button(window, text="Sign up", command=user_signup).place(x=270,y=230)


window.mainloop()