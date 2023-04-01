import csv
import openpyxl 


with open('new_input_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    data = [row[:2] + row[3:] for row in reader]  

book = openpyxl.Workbook()
sheet = book.active
sheet.title = 'Data'

sheet['A2'] = 'ID'
sheet['A3'] = 'Name'
sheet['A4'] = 'Phone number'
sheet['B1'] = 'Person 1'
sheet['C1'] = 'Person 2'
sheet['D1'] = 'Person 3'
sheet['E1'] = 'Person 4'
sheet['F1'] = 'Person 5'
sheet['G1'] = 'Person 6'

for i, row in enumerate(data):
    for j, value in enumerate(row):
        sheet.cell(row=j+2, column=i+2, value=value)


book.save('brend_new_input_data.xlsx')
