from _16_data_analysis_pyecharts.data_define import Record
from file_utils import *
from pyecharts.charts import Bar
from pyecharts.options import *

# 读取数据
text_file_reader = TextFileReader("../data/数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("../data/数据分析案例/2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_file()
feb_data = json_file_reader.read_file()

# all_data=jan_data+feb_data
jan_data.extend(feb_data)

# 计算每天的销售额
data_dict={}
for record in jan_data:
    if record.date in data_dict.keys():
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date]=record.money

print(data_dict)

# 可视化
bar = Bar(init_opts=InitOpts(theme="light"))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="2011年1月和2月销售额"),
)

bar.render()