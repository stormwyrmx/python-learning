import pickle

"""
pickle和json的区别：
    - pickle可以序列化python的任意对象，包括函数，类，对象等
    - json只能序列化python的基本数据类型，不能序列化函数，类，对象等
    - pickle序列化的结果是字节码类型是<class 'byte'>，json序列化的结果是字符串，类型是<class 'str'>
    - pickle.load()和json.load()读入可以是不同的类型，这里的数据类型是<class 'dict'>
"""

def pickle_test():
    data={"name":"husiqi","age":20,"size":103}
    pickle_dumps = pickle.dumps(data)
    print(pickle_dumps)
    print(type(pickle_dumps))
    data2=pickle.loads(pickle_dumps)
    print(data2)
    print(type(data2))

def pickle_file_test():
    with open('data.pkl','wb') as f:
        data={"name":"husiqi","age":22,"size":103}
        pickle.dump(data,f)
    with open('data.pkl','rb') as f:
        data=pickle.load(f)
        print(data)
        print(type(data))

if __name__ == '__main__':
    pickle_test()
    # pickle_file_test()