# excel_row_merger
# Tuomas Eerola 2021
#
# Keep the value of the index Column. Merge other cells without losing data.

import pandas as pd

excel_workbook = 'original_excel.xlsx'

sheet1 = pd.read_excel(excel_workbook, sheet_name='Sheet1')
grouped = sheet1.groupby(by='index_column_name').sum()

print(grouped)

grouped.to_excel('merged_excel.xlsx')
