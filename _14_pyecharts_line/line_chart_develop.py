import json
from pathlib import Path
from pyecharts.charts import Line
from pyecharts.options import *

# 读取美国、日本、印度疫情数据
us_path = Path("../data/可视化案例数据/折线图数据/美国.txt")
jp_path = Path("../data/可视化案例数据/折线图数据/日本.txt")
in_path = Path("../data/可视化案例数据/折线图数据/印度.txt")

us_data = us_path.read_text('utf-8')[26:-2]
jp_data = jp_path.read_text('utf-8')[26:-2]
in_data = in_path.read_text('utf-8')[26:-2]

us_dict=json.loads(us_data)
jp_dict=json.loads(jp_data)
in_dict=json.loads(in_data)

us_trend_data=us_dict['data'][0]['trend']
jp_trend_data=jp_dict['data'][0]['trend']
in_trend_data=in_dict['data'][0]['trend']

us_x_data=us_trend_data.get('updateDate')[:314]
us_y_data=us_trend_data['list'][0]['data'][:314]
jp_x_data=jp_trend_data.get('updateDate')[:314]
jp_y_data=jp_trend_data['list'][0]['data'][:314]
in_x_data=in_trend_data.get('updateDate')[:314]
in_y_data=in_trend_data['list'][0]['data'][:314]

# 生成折线图
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊病例", y_axis=us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊病例", y_axis=jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊病例", y_axis=in_y_data,label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美国、日本、印度确诊病例",pos_left="center",pos_bottom="bottom"),
)

line.render("render.html")

