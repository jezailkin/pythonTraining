# 2
# list= [1,2,4,6,7,9,5,3]
# count=0
# for i in list:
#     count+=1
#     print(count)
# 3
# num_ls=[10,15,17,18,20,22,40]
# for num in num_ls:
#     if num % 2 == 0:
#         print(num)
# 4
# num_list=[11,12,8,5,67,30,4,0,100]
# count=0
#
# for num in num_list:
#     if num >= 10:
#         count +=1
# print(count)
# 5
# numbers = []
# count = int(input("How many numbers do you want to enter? "))
#
# for _ in range(count):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# total_sum = 0
# for number in numbers:
#     total_sum += number
#
# if count > 0:
#     average = total_sum / count
#     print("The average is:", average)
# else:
#     print("No numbers entered.")
# 6
# list=[1,2,-5,-7,-15,18,22,35]
# positive_list=[]
#
# for num in list :
#     if num > 0:
#         positive_list.append(num)
#
# print(positive_list)
# 7
# numbers= [1,2,22,800,444,3,66,1000,9999]
# biggest= numbers[0]
#
# for num in numbers :
#     if num > biggest:
#         biggest = num
# print(f'largest is {biggest}')
# 8
# ls = [1, 2, 3, -5, 343, -6, 33, 1, 78, 90, -1, 1, 1, 1]
# result = []
# current = []
# counter = 0
# for i in ls:
#     counter += 1
#     if i > 0:
#         current.append(i)
#     elif i < 0 and len(current) > 0:
#         result.append(current)
#         current = []
#     if counter == len(ls) - 1:
#         result.append(current)
# print(result)
# # result.sort(reverse=True)
# # big_ls = result[0]
# big = 0
# final_ls = []
#
# for i in result:
#     if len(i) > big:
#         final_ls = i.copy()
#         big = len(i)
# print(final_ls)
# sum = 0
# for i in final_ls:
#     sum += i
# print(f"result:{sum}")
# 9
# numbers = [1, 5, 4, 3, 4, 5, -4, -5, -6, -8, -3]  # Original list
#
# i = 0
# while True:
#     try:
#         if numbers[i] < 0:
#             numbers.remove(numbers[i])
#         else:
#             i += 1
#     except IndexError:
#         break
#
# print(numbers)
# 10
