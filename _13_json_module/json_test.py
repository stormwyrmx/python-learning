import json


data={
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
# python字典数据转json字符串
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)

# json字符串转python字典
json_str2='{"name":"husiqi","age":17}'
data2=json.loads(json_str2)
print(data2)
print(type(data2))

# python元组转json字符串
data3=(1,2,3)
json_str3=json.dumps(data3)
print(json_str3)
print(type(json_str3))
print(data3)
print(type(data3))