import os
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def analyze_sensor_data(folder_path):
    plt.rcParams['font.family'] = 'SimHei'
    file_types = {
        'dataV.txt': 'Vertical Sensor',
        'dataH.txt': 'Horizontal Sensor 1'
    }

    for file_name, sensor_type in file_types.items():
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            continue

        # 读取数据
        df = pd.read_csv(
            file_path,
            sep='\s+',
            header=None,
            parse_dates=[[0, 1]],
            date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
        )
        columns = ['Timestamp'] + [f'Value_{i}' for i in range(1, len(df.columns))]
        df.columns = columns

        # 处理前四列数据
        for col in df.columns[1:5]:  # 处理Value_1到Value_4
            waveform = df[col]
            
            # 生成统计报告
            stats = {
                '最大值': waveform.max(),
                '最小值': waveform.min(),
                '极差': waveform.max() - waveform.min(),
                '平均值': waveform.mean(),
                '标准差': waveform.std()
            }
            
            # 保存结果
            result_file = os.path.join(folder_path, f"{sensor_type}_{col}_report.txt")
            with open(result_file, 'w') as f:
                f.write(f"""=== {sensor_type} {col} 数据分析报告 ===
时间范围：{df.Timestamp.min()} 至 {df.Timestamp.max()}
采样点数：{len(waveform)}
最大波动值：{stats['最大值']:.4f}
最小波动值：{stats['最小值']:.4f}
极差：{stats['极差']:.4f}
平均稳定值：{stats['平均值']:.4f} ± {stats['标准差']:.4f}
""")

            # 生成图表
            plt.figure(figsize=(10,4))
            plt.plot(df['Timestamp'], waveform, 'b-', linewidth=1)
            plt.title(f'{sensor_type} {col} Time Series\n({df.Timestamp.dt.date.iloc[0]})')
            plt.xlabel('Time')
            plt.ylabel('Measurement')
            plt.grid(True)
            
            plot_path = os.path.join(folder_path, f"{sensor_type}_{col}_analysis.png")
            plt.savefig(plot_path, dpi=300)
            plt.close()

# GUI选择文件夹
root = Tk()
root.withdraw()
selected_folder = filedialog.askdirectory(title="选择数据文件夹（如5.10, 5.11等）")

if selected_folder:
    analyze_sensor_data(selected_folder)
    print(f"处理完成！结果保存在：\n{selected_folder}")
    print("生成的文件：")
    for f in os.listdir(selected_folder):
        if f.endswith(('.png', '.txt')):
            print(f" - {f}")
else:
    print("未选择文件夹")