import csv

data = [{'fullname': 'noa brik', 'ID': 1000 , 'startyear': 2020, 'salary': 9000},
        {'fullname': 'belly david', 'ID': 1001 , 'startyear': 2018, 'salary': 8500}
    , {'fullname': 'prada gucci', 'ID': 1002 , 'startyear': 2013, 'salary': 9300}
    , {'fullname': 'moana toy', 'ID': 1003 , 'startyear': 2000, 'salary': 15000}
    , {'fullname': 'shrik sharlot' , 'ID': 1004 , 'startyear': 2023, 'salary': 6000}
    , {'fullname': 'sharol pretz', 'ID': 1005 , 'startyear': 2025, 'salary': 4500}]

field_names = ['fullname', 'ID', 'startyear', 'salary']

with open('salary_depends_on_startyear.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)



    # file_name = 'students_records_v2.csv'
    # field_names = ['Full Name', 'ID', 'Year', 'Salary']
    #
    # data = [
    #     {field_names[0]: 'John Due', field_names[1]: 0, field_names[2]: 1999, field_names[3]: 9000},
    #     {field_names[0]: 'Leo Messi', field_names[1]: 0, field_names[2]: 2001, field_names[3]: 9001},
    #     {field_names[0]: 'Luna Hasson', field_names[1]: 0, field_names[2]: 2005, field_names[3]: 8977},
    #     {field_names[0]: 'Lora Daxa', field_names[1]: 0, field_names[2]: 2012, field_names[3]: 9010},
    #     {field_names[0]: 'Maram Hasson', field_names[1]: 0, field_names[2]: 2001, field_names[3]: 9000},
    #
    # ]
    #
    # with open(file_name, 'w', newline='') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=field_names)
    #     writer.writeheader()
    #     writer.writerows(data)