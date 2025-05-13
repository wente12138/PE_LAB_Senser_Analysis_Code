# 传感器数据分析程序 - analysis_diff_data.py

## 📖 使用说明

### 0. 数据格式
```
.
├── 5.10
│   ├── dataH.txt
│   └── dataV.txt
├── 5.11
│   ├── dataH.txt
│   └── dataV.txt
└── 5.12
    ├── dataH.txt
    └── dataV.txt
```

请记得将数据备份后，对有三列有效数据的文件命名为`dataV.txt`；
对有四列有效数据的文件命名为`dataH.txt`。


### 1. 程序功能
- 自动处理竖直传感器（dataV.txt）和水平传感器（dataH.txt）数据
- 为每个传感器的前4列数据生成：
  - 时序波形图（PNG格式，300dpi高清图）
  - 详细统计报告（包含最大值/最小值/极差等指标）
- 自动识别日期文件夹结构

### 2. 运行环境
- Python 3.8+
- 必需库：`pandas`, `matplotlib`, `tkinter`

### 3. 安装依赖
```bash
pip install pandas matplotlib
```

### 4. 使用流程
[开启一个新的终端，在cd到代码所在文件夹，]
```bash
python analysis_diff_data.py
```
1. 程序启动后自动弹出文件对话框
2. 选择目标日期文件夹（如`testdata`）
3. 点击"选择文件夹"



### 5. 输出文件
在选中的日期文件夹内生成：
```
├── Vertical_Sensor_Value_{1-4}_analysis.png
├── Vertical_Sensor_Value_{1-4}_report.txt
├── Horizontal_Sensor_1_Value_{1-4}_analysis.png
└── Horizontal_Sensor_1_Value_{1-4}_report.txt
```

### 6. 文件命名规则
| 文件类型 | 命名格式 | 示例 |
|---------|----------|------|
| 竖直传感器图表 | `Vertical_Sensor_Value_{n}_analysis.png` | Vertical_Sensor_Value_1_analysis.png |
| 水平传感器报告 | `Horizontal_Sensor_1_Value_{n}_report.txt` | Horizontal_Sensor_1_Value_1_report.txt |

### 7. 示例输出
```bash
处理完成！结果保存在：
C:/User/your_path/5.10
生成文件：
 - Vertical_Sensor_Value_1_analysis.png
 - Vertical_Sensor_Value_1_report.txt
 - Horizontal_Sensor_1_Value_1_analysis.png
 - ...
```

### 8. 报告内容示例
```text
=== Value_1 数据分析报告 ===
时间范围：2025-05-10 08:00:01 至 2025-05-10 08:00:01
采样点数：2
最大波动值：449.3735
最小波动值：449.3679
极差：0.0056
平均稳定值：449.3707 ± 0.0028
```

### 9. 注意事项
1. 确保目标文件夹包含至少一个数据文件
2. 数据文件必须命名为`dataV.txt`或`dataH.txt`
3. 支持同时处理多个传感器数据文件
4. 空数据列会自动跳过处理
5. 图表尺寸为10x4英寸，适合直接插入报告


```
*注：实际文件路径会根据选择目录自动调整，建议每次处理单个日期文件夹*