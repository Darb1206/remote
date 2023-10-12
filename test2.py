import csv

# 读取CSV文件
csv_filename = "fyx_chinamoney.csv"  # 替换成你的CSV文件名
data = []
with open(csv_filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        data.append(row)

# 设置每个批次的大小
batch_size = 80

# 拆分数据成多个批次并打印输出
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    print(f"Batch {i // batch_size + 1}: {batch}")

