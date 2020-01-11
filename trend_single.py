import tushare as ts
import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

day_k = ts.get_hist_data('600787') #一次性获取全部日k线数据

# stockbasic = ts.get_report_data(2019,2)
# price_now = ts.get_today_all()
# total = stockbasic.merge(price_now)
# total.to_excel("stock_basic.xlsx")

list_data = [day_k.loc[:"2019-01-01", "open"]]

# Plot
ax = sns.lineplot(data=list_data)

# Rotate x labels in case too densely positioned dates
ax.set_xticks(ax.get_xticks()[::10])
plt.xticks(rotation=45)
plt.xlabel("date")
plt.ylabel("Opening price")
plt.show()