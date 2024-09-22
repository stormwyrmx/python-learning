# 基本捕获语法
try:
    a:int=1/0
except:
    print("不能被0除!")
else:
    print(a)
finally:
    print("finally")

# 捕获指定异常
try:
    name
except NameError:
    print("name没有定义")

# 捕获多个异常
try:
    name
except (NameError,ZeroDivisionError) as e:
    print(e)

# 捕获所有异常
try:
    fuck=1/0
except Exception as e:
    print(e)