import json

def json_test():
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
    json_str = json.dumps(data,ensure_ascii=False)  # dumps to json
    print(json_str)

    # json字符串转python字典
    json_str2='{"name":"husiqi","age":"17"}'
    data2=json.loads(json_str2)  # loads from json
    print(data2)
    print(type(data2))

    # python元组转json字符串
    data3=(1,2,3)
    json_str3=json.dumps(data3)
    print(json_str3)
    print(type(json_str3))
    print(data3)
    print(type(data3))

def json_file_test():
    with open('data.json','w',encoding='utf-8') as f:
        data={"name":"husiqi","age":20,"size":103}
        json.dump(data,f,ensure_ascii=False)
    with open('data.json','r',encoding='utf-8') as f:
        data=json.load(f)
        print(data)
        print(data['name'],data['age'],data['size'])
        print(type(data))

if __name__ == '__main__':
    # json_file_test()
    json_test()