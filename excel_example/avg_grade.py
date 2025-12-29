import csv

from excel_example.exercise_excel import field_names

file_name = 'avg_grade.csv'
field_names = ['year','grade']

data = [
    {field_names[0]:0 , field_names[1]: 80 },
    {field_names[0]: 0, field_names[1]: 90 },
    {field_names[0]: 0, field_names[1]:95 },
    {field_names[0]: 0, field_names[1]: 85 },
    {field_names[0]: 0, field_names[1]: 78 },
]

counter = 0
for year in range (2000 , 2005):
    data[counter][field_names[1]] = year
    counter+=1

if field_names[1] == 90 :



 with open(file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)