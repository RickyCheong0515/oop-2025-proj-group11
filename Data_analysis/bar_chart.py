import pandas as pd
import matplotlib.pyplot as plt

# 讀取資料
df = pd.read_csv('Sales_all.csv')

# 確保「交易年月日」為日期格式
df['交易年月日'] = pd.to_datetime(df['交易年月日'])
# str >> datatime

# 將單價欄轉為數值型態，避免錯誤
df['單價元平方公尺'] = pd.to_numeric(df['單價元平方公尺'], errors='coerce')

# 按鄉鎮市區分組，計算平均單價
avg_price_by_area = df.groupby('鄉鎮市區')['單價元平方公尺'].mean().sort_values(ascending=False)

# 畫出長條圖
plt.figure(figsize=(15, 8))
avg_price_by_area.plot(kind='bar')
