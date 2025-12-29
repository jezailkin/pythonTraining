# 1
# num = int(input("Enter a number: "))
# for i in range (num + 1):
#     if i % 2 == 0:
#         print(i)
#         print("even number")
#
# for i in range(num + 1):
#     if i % 2 != 0:
#         print(i)
#         print("odd number")
# 2
# sum =0
# for i in range(1,27):
#     sum += i
#     print("added",i,"current sum is",sum )
# 3
# name = input("enter your name")
# char = input("enter your char")
# tv = 0
# for i in name:
#     if char == i  :
#         tv += 1
# print(tv)
# 4
# for i in range(1000, 5000, 4):
#     if i % 3 == 0:
#         print(i)
# 5.1
# email=input("Enter your email: ")
# if email.count("@") ==1 and email.endswith(".com") ==1:
#     print("valid email")
# else:
#     print("invalid email")
# 5.2
# mail = input("Please enter your email: ")
# end_mail = mail[len(mail) - 4:len(mail) ]
# at_count = 0
# for i in mail:
#     if i == "@":
#         at_count += 1
# if at_count == 1 and end_mail == ".com":
#     print("valid email")
# else:
#     print("invalid email")
# 6
# for i in range(1,11):
#     for j in range (1,11):
#         print(i*j, end="\t")
#     print()
# 7
# for i in range (100,500):
#     if i == 372 :
#         break
#     print (i)
# 8
# for i in range(10,77):
#     if i == 32 or i==50 or i==70:
#         continue
#     print (i)
# 9
# num_range= int(input("Enter a number"))
# num1=1
# num2=1
# for i in range(num_range):
#     num1=num2-num1
#     num2=num1+num2
#     print(num2)
# 10
# num= int(input("type in a num"))
# if num == 0:
#     print(0)
# elif num == 1:
#     print(1)
# else:
#     a, b = 0, 1
#     for _ in range(2, num+1):
#         a, b = b, a + b
#     print(b)
# 11
# 15
num= input("enter your number")
for i in range(2,num):
    if num % i==0:
        break
    print(i)
