import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'

# 读取数据
df = pd.read_csv(
    'data.txt',
    sep='\s+',
    header=None,
    parse_dates=[[0, 1]],
    date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
)

# 设置列名（根据数据示例，时间戳后应包含9列数据）
columns = ['Timestamp'] + [f'Value_{i}' for i in range(1, 10)]
df.columns = columns

# 为前四列传感器数据生成统计报告和图表
for col_idx in range(1, 5):  # 处理Value_1到Value_4
    col_name = f'Value_{col_idx}'
    data = df[col_name]
    
    # 计算统计指标
    stats = {
        '最大值': data.max(),
        '最小值': data.min(),
        '极差': data.max() - data.min(),  # 手动计算极差
        '平均值': data.mean(),
        '标准差': data.std()
    }
    
    # 生成报告
    report = f"""
=== {col_name} 数据分析报告 ===
时间范围：{df.Timestamp.min()} 至 {df.Timestamp.max()}
采样点数：{len(data)}
最大波动值：{stats['最大值']:.4f}
最小波动值：{stats['最小值']:.4f}
极差：{stats['极差']:.4f}
平均稳定值：{stats['平均值']:.4f} ± {stats['标准差']:.4f}
"""
    print(report)
    
    # 保存图表
    plt.figure(figsize=(10,4))
    plt.plot(df['Timestamp'], data, 'b-', linewidth=1)
    plt.title(f'Sensor {col_idx} Time Series (2025-05-10)', fontsize=12)
    plt.xlabel('Timestamp')
    plt.ylabel('Measurement')
    plt.grid(True)
    plt.savefig(f'sensor_{col_name}_analysis.png', dpi=300)
    plt.close()

print("四张图表已生成：")
for i in range(1,5):
    print(f" - sensor_Value_{i}_analysis.png")