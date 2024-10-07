import pandas as pd

# Đường dẫn tới file CSV
#file_path = 'F:/3.5 Years/Second Year/Dataset/Bank_Churn.csv'

# Đọc file CSV
#df = pd.read_csv(file_path)

# In dữ liệu để kiểm tra
#print(df.head())

# đọc csv
import csv
with open ('F:/3.5 Years/Second Year/Dataset/Bank_Churn.csv','r') as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        print(row)