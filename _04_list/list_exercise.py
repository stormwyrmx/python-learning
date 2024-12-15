list=[21,25,21,23,22,20]
list.append(31)
list.extend([29,33,30])
print(list)
pop1 = list.pop(0)
print(pop1)
pop2 = list.pop()
print(pop2)
print(list.index(31))

# 测试unpacking/multiple assignment
a,b=([[1,3],[1,4]],[2,4])
print(a)
print(b)

c,d={'hu':'555','li':'666'}
print(c)
print(d)


def test():
    a=1
    b=2
    return a,b


print(test())
print(type(test()))