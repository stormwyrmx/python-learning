from pyecharts.charts import Line
from pyecharts.options import *



line = Line()
line.add_xaxis(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
line.add_yaxis("week day", [6, 9, 8, 8, 7, 6, 7])

line.set_global_opts(
    title_opts=TitleOpts(True,"Line-基本示例"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True, max_=10, min_=5)
    
)

line.render("line_chart_test.html")