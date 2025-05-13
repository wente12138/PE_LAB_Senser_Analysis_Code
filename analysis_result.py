import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'  # 替换为你选择的字体

 
# 哪里需要显示中文就在哪里设置
# 读取数据并自动处理时间
df = pd.read_csv(
    'data.txt',
    sep='\s+',  # 匹配任意空白分割
    header=None,
    parse_dates=[[0, 1]],  # 合并前两列为时间
    date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
)

# 自动生成列名（根据实际列数）
columns = ['Timestamp'] + [f'Value_{i}' for i in range(1, len(df.columns))]
df.columns = columns

# 验证数据结构和列数
print("数据列结构：")
print(df.head(2))
print(f"\n总列数：{len(df.columns)}")

# 提取第三列数据（对应Value_2）
waveform = df['Value_2']

# 计算统计指标（修正极差计算）
stats = {
    '最大值': waveform.max(),
    '最小值': waveform.min(),
    '极差': waveform.max() - waveform.min(),  # 修正此处
    '平均值': waveform.mean(),
    '标准差': waveform.std()
}

# 生成分析报告
report = f"""\n
=== 传感器数据分析报告 ===
时间范围：{df.Timestamp.min()} 至 {df.Timestamp.max()}
采样点数：{len(waveform)}
最大波动值：{stats['最大值']:.4f}
最小波动值：{stats['最小值']:.4f}
极差：{stats['极差']:.4f}
平均稳定值：{stats['平均值']:.4f} ± {stats['标准差']:.4f}
"""
print(report)

# 保存结果和波形图
df[['Timestamp', 'Value_2']].to_csv('analysis_results.csv', index=False)
plt.figure(figsize=(10,4))
plt.plot(df['Timestamp'], waveform, 'b-', linewidth=1)
plt.title('传感器第三列时序数据 (2025-05-10)')
plt.xlabel('时间')
plt.ylabel('测量值')
plt.grid(True)
plt.savefig('sensor_analysis.png', dpi=300)
print("结果已保存：analysis_results.csv 和 sensor_analysis.png")