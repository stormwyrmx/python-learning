employees={
    '王力宏':{
        '部门':"科技部",
        '工资':3000,
        '级别':1
    },
    '周杰伦':{
        '部门':"市场部",
        '工资':5000,
        '级别':2
    },
    '林俊杰':{
        '部门':"市场部",
        '工资':7000,
        '级别':3
    },
    '张学友':{
        '部门':"科技部",
        '工资':4000,
        '级别':1
    },
    '刘德华':{
        '部门':"市场部",
        '工资':6000,
        '级别':2
    },
}

employees_names = employees.keys()
for name in employees_names:
    if employees.get(name).get('级别') == 1:
        employees[name]['级别'] += 1
        employees.get(name)['工资'] += 1000

print(employees)


c = {'hu': '555', 'li': '666'}
for key, value in c.items():
    print(key)
    print(value)