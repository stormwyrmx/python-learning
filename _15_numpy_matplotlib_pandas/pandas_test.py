import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
数据分析，可视化数据规律
数据前处理，为 AI 模型展平道路
使用 Pandas 做深度学习中的数据处理部分
Numpy 的是没有任何数据标签信息的，你可以认为它是纯数据。而 Pandas 就像字典一样，还记录着数据的外围信息
"""

def read_excel():
    # DataFrame是Pandas库中的一种数据结构，类似于Excel表格，可以存储多种类型的数据
    df = pd.read_excel('各手机销量表.xlsx', index_col=0)
    print(df)
    df.loc['小米'] = 3000  # loc stands for location. 用于通过标签索引来访问数据。链式赋值可能会有问题！
    print(df)
    # df.iloc[0][df.columns.get_loc('销量')] = [2000]  # iloc stands for index location. 用于通过整数位置索引来访问数据
    # print(df)

    # # Runtime Configuration Parameters
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.figure(figsize=(10, 6))
    #
    # labels = df['品牌']
    # y = df['销量']
    # #                         automatic percentage
    # plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
    # plt.title('各手机品牌销量占比')
    # # plt.axis('equal')
    # plt.show()


def read_csv():
    pd.read_csv('各手机销量表.csv')


def pandas_series():
    list1=[1, 3, 5, np.nan, 6, 8]
    series = pd.Series(list1)
    print(series)
    series = pd.Series(list1, index=["a", "b", "c", "d", "e", "f"])
    print(series)
    series = pd.Series({'a': 1, 'b': 2, 'c': 3})
    print(series)

    print(series.to_numpy())
    print(series.keys())
    print(series.values)

    print(series.loc['a':'c'])  # 选择a到c的数据
    print(series.iloc[0:2])  # 选择前两个数据


def pandas_dataframe_create():
    # print(np.random.randn(5))
    data_frame = pd.DataFrame([[1, 2, 3, 4, 5],[6, 7, 8,9,10]])
    print(data_frame)
    # 其实字典中的 key 会被当成是数据中的 column，而 value 会被当做是 row，
    # 这个非常符合你在 Excel 中的使用习惯。 因为往往随着数据量变大，你用鼠标滚轮滚动查看不同数据的时候，天然的比较喜欢上下查看不同的数据样本，而不是左右查看，
    # 所以一般都是左右记的是数据标签（特征）， 上下排列的是不同数据样本。
    df=pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    print(df)
    df = pd.DataFrame({"col1": pd.Series([1, 3]), "col2": pd.Series([2, 4])})
    print(df)
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
    print(df)
    print(df.index)
    print(df.columns)

    data_frame = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'),index=pd.date_range('20210101', periods=5))
    print(data_frame)

    my_json_data = [
        {"age": 12, "height": 111},
        {"age": 13, "height": 123}
    ]
    print(pd.DataFrame(my_json_data, index=["jack", "rose"]))

    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
    print(df.to_numpy())

def pandas_dataframe_select():
    data = np.arange(-12, 12).reshape((6, 4))
    # print("numpy:\n", data[:, [1,2]])
    df = pd.DataFrame(
        data,
        index=list("abcdef"),
        columns=list("ABCD"))
    print(df)
    print(df[["C", "B"]])  # 选择多列
    print(df.loc["a":"c", "A":"C"])  # 选择a到c行(包含c行)，A到C列更贴切 Excel 中的使用原则。用字母表示就是左右都是闭区间
    print(df.loc['a':'c', :])  # 选择多行多列。每一个,隔开的部分都是一个维度（都可以当做一个列表的切片）

    print(df.iloc[0:3, 1:3])  # 选择0到2行，1到2列
    print(df.iloc[[1,2], :])  # 选择1和2行，所有列

    row_labels = df.index[2:4]
    print(row_labels)
    col_labels = df.columns[[0, 3]]
    print(df.loc[row_labels, col_labels])

    indexer = df.columns.get_indexer(["A", "C"])
    print(df.iloc[:2,indexer])


def pandas_dataframe_functions():
    data = np.array([[1.39, 1.77, None], [0.34, 1.91, -0.05], [0.34, 1.47, 1.22], [None, 0.27, -0.61]])
    df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three'])
    print(df)
    print(df.keys())  # 返回列名
    print(df.columns)
    print(df.index)
    print(df.values,type(df.values))  # 返回数据（二维数组）
    print(df.dropna(axis=0))  # 删除包含 NaN 的行
    print(df.fillna(0))


    df1 = pd.DataFrame(np.random.random((4, 3)), columns=["c0", "c1", "c2"])
    print(df1)
    print("\ndescribe:\n", df1.describe())
    print(df1.mean())
    print(df1.mean(axis=1))  # 第0个维度是列，第1个维度是行。和numpy不一样
    print(df1.std())


if __name__ == '__main__':
    # read_excel()
    # pandas_series()
    # pandas_dataframe_create()
    # pandas_dataframe_select()
    pandas_dataframe_functions()
