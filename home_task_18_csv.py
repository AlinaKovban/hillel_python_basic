import json
import csv
import random

with open('input_data.json', 'r') as f:
    data = json.load(f)

with open('new_input_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Age', 'Phone number'])
    
    for key, value in data.items():
        row = [key] + list(value) + [random.randint(1000000, 9999999)]
        writer.writerow(row)

