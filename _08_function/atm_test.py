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

