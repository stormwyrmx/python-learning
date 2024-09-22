import pandas as pd
import matplotlib.pyplot as plt

# DataFrame是Pandas库中的一种数据结构，类似于Excel表格，可以存储多种类型的数据
df = pd.read_excel('各手机销量表.xlsx')
# Runtime Configuration Parameters
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 6))

labels = df['品牌']
y = df['销量']
#                         automatic percentage
plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('各手机品牌销量占比')
# plt.axis('equal')
plt.show()

