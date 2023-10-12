import requests
from bs4 import BeautifulSoup
import csv


# 网页数据爬取
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
response = requests.get(url)
html = response.text

# 数据筛选
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')  # 假设数据在表格中

# 数据提取
selected_data = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 6:
        # 假设列的顺序为 ISIN, Bond Code, Issuer, Bond Type, Issue Date, Latest Rating
        isin, bond_code, issuer, bond_type, issue_date, rating = [col.text for col in columns]
        if bond_type == 'Treasury Bond' and '2023' in issue_date:
            selected_data.append([isin, bond_code, issuer, bond_type, issue_date, rating])

# CSV 文件处理
with open('bond_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
    csv_writer.writerows(selected_data)
