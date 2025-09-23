a="1"
b=2
a+str(b)

print(a,b)

name="yuki asuna"
age=16
level=10.5
print("我叫%s,今年%d岁,等级%.1f"%(name,age,level))
print("我叫{},今年{}岁,等级{}".format(name,age,level))
print("我叫{0},今年{1}岁,等级{2}".format(name,age,level))
message=f"我叫{name.title()},今年{age}岁,等级{level}"
print(message)
message2=r"我叫小琪琪，今年17岁啦！\n"  # r表示原始字符串raw string，不会转义
# A raw string treats backslashes as literal characters and does not interpret them as escape characters
print(message2)
