import pandas as pd

xlsx_file = r'D:\G. Python\xlsxtocsv\pupuk.xlsx'
csv_file = r'D:\G. Python\xlsxtocsv\pupuk.csv'

data = pd.read_excel(xlsx_file)

data.to_csv(csv_file, index=False)

print(f"File {xlsx_file} berhasil di konversi menjadi {csv_file}")