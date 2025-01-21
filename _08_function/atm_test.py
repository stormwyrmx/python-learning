# In Python, functions can be defined before or after the variables they use,
# as long as the variables are defined before the function is called.
money=500_000
print(money)
name=input("请输入你的名字：")
def show_menu():
    """
    显示主菜单
    :return: 选择的值(1~4)
    """
    print("---------------主菜单------------------")
    print(f"{name}您好,欢迎HSBC银行")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    return input("请输入您的选择：")

def query_balance(show_header):
    if show_header:
        print("---------------查询余额------------------")
    print(f"{name}您好,您的余额是：{money}元")

def deposit():
    print("---------------存款------------------")
    deposit_money = int(input("请输入存款金额："))
    # .函数中变量的作用域:
    # 创建于函数外部，它是全局（Global）的，它在这个py文件内部的任何地方可见。
    # 创建于函数内部，它是局部（Local）的，它只能在函数内部才能访问，在函数外部不可见。
    # 全局变量和局部变量重名，函数内会访问到局部变量，函数外访问到全局变量。
    # 函数内部能访问全局变量，但不能修改！
    # 如果非要在函数内部修改全局变量，需要声明global⭐
    global money
    money += deposit_money
    print(f"{name}您好,您成功存款{deposit_money}元")
    query_balance(False)

def withdraw():
    print("---------------取款------------------")
    withdraw_money = int(input("请输入取款金额："))
    global money
    if withdraw_money > money:
        print("余额不足")
    else:
        money -= withdraw_money
        print(f"{name}您好,您成功取款{withdraw_money}元")
        query_balance(False)

flag=True
while flag:
    choice=show_menu()
    if choice=='1':
        query_balance(True)
    elif choice=='2':
        deposit()
    elif choice=='3':
        withdraw()
    elif choice=='4':
        print("欢迎下次再来")
        flag=False
    else:
        print("输入错误，请重新输入")


