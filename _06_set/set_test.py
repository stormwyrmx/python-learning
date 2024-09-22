my_list=['黑马程序员','传智教育','黑马程序员','传智教育','itheima','itcast','itheima','itcast','best']
my_set=set()
for element in my_list:
    my_set.add(element)
print(f"有列表:{my_list}")
print(f"存入集合后的结果:{my_set}")

my_set2=set(my_list)
print(my_set2)

my_set3={element for element in my_list}
print(my_set3)

