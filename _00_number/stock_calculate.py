name="阿里巴巴"
stock_price=73.10
stock_code="09988"
stock_price_daily_growth_factor=1.02
growth_days = input("请输入增长天数：")
stock=stock_price*(stock_price_daily_growth_factor**int(growth_days))
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.2f，经过%d天的增长，股价是：%.2f"%(stock_price_daily_growth_factor,int(growth_days),stock))
