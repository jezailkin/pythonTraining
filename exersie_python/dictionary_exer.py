# grades = [70,90,88,98,68,84,93,77,83,97]
# total = 0
# max_grade = grades[0]
# min_grade = grades[0]
# counter = 0
#
# for grade in grades:
#     total += grade
#
#     if grade > max_grade:
#         max_grade = grade
#     else:
#         if grade < min_grade:
#             min_grade = grade
#
#     if grade > 70 and grade < 90:
#         counter += 1
#
#
# avg = total / len(grades)
# print(f"highest grade: {max_grade}")
# print(f"lowest grade: {min_grade}")
# print(f"average:{avg}")
# print(f"grades between 70 and 90: {counter}")
# 2
# list= [10,23,34,45,56,67,78,89]
# total_num= sum(list)
# num = len(list)
#
# avg_num = total_num/num
# print(avg_num)
# 3
# list = [15,20,20,60,60,30,56,56,75]
# new_list = []
# for i in list :
#     if i not in new_list :
#         new_list.append(i)
# print(new_list)
# 4
# list= [1,2,3,4,5,6,7,8,9]
# multiply = 1
# for i in list:
#     multiply *= i
# print(multiply)
# 5
# dictionary = {
#     "name1":"lona",
#     "name2":"bylsan",
#     "name3":"noor"
# }
# for key in dictionary.keys():
#     print(dictionary.get(key))
# 6
students =[{"name":"mor" , "age":25, "id":1 , "grades":[60,79,80,90]},
           {"name":"bil","age":24,"id":2,"grades":[65,55,77,80]}
    ]

max = 0
sum = 0

for values in students:
    if values["grades"][sum] > max:
        max = values["grades"][sum]
        print(max)
