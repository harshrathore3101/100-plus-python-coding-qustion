# 1.1 Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.
# inp_txt1 = input('Enter an integer: ')
# inp_int = int(inp_txt1)
# inp_txt2 = input('Enter an float: ')
# inp_float = float(inp_txt2)
# print(inp_int * inp_float)

# 1.2 Take two numbers from the users. Calculate the result of second number power of the first number.
# inp_txt1 = int(input('Enter a Number: '))
# inp_txt2 = int(input('Enter a Number: '))
# print(inp_txt1 ** inp_txt2)
# print(pow(inp_txt1 , inp_txt2))

# 1.3 Create a random number between 0 to 10
# import random
# print(random.randint(0,10))

# 1.4 Find the floor division of two numbers.
# import math
# inp_txt1 = int(input('Enter a Number: '))
# inp_txt2 = int(input('Enter a another Number: '))
# print(math.floor(inp_txt1/inp_txt2))
# print(inp_txt1//inp_txt2)

# 1.5 Swap two variables. To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.
# inp_txt1 = input('Enter a Number: ')
# inp_txt2 = input('Enter a another Number: ')
# print(inp_txt1,inp_txt2)
# swap_txt3 = inp_txt1
# inp_txt1 = inp_txt2
# inp_txt2 = swap_txt3
# print(inp_txt1,inp_txt2)

# 2.1 Find the max number of two numbers.
# inp_txt1 = int(input('Enter a Number: '))
# inp_txt2 = int(input('Enter a another Number: '))
# if inp_txt1 > inp_txt2:
#     print(inp_txt1)
# else:
#     print(inp_txt2)

# 2.2 Find the largest of the three numbers.
# inp_txt1 = int(input('Enter a Number: '))
# inp_txt2 = int(input('Enter a another Number: '))
# inp_txt3 = int(input('Enter a another another Number: '))
# if inp_txt1 > inp_txt2:
#     if inp_txt1 > inp_txt3:
#         print(inp_txt1)
# elif inp_txt2 > inp_txt3:
#         print(inp_txt2)
# else:
#     print(inp_txt3)

# 2.3 Take numbers from a user and show the average of the numbers the user entered.
# inp_txt1 = int(input('Enter a Number: '))
# inp_txt2 = int(input('Enter a another Number: '))
# inp_txt3 = int(input('Enter a another another Number: '))
# avg = ((inp_txt1 + inp_txt2 + inp_txt3 )/ 3)
# print(int(avg))

# 2.4 For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.
# inp_txt1 = int(input('Enter a Number: '))
# NOs = []
# for no in range(1,inp_txt1):
#     if no % 3 == 0 and no % 5 == 0:
#         NOs.append(no)
# print(NOs)

# 2.5 For a given list, get the sum of each number in the list
# arr = [1, 2, 3, 4]
# sum = 0
# for no in arr:
#     sum = sum + no
# print(sum)
# or
# print(sum(arr))

# 3.1 For a given list, get the sum of each number in the list
# arr = [1, 2, 3, 4]
# sum = 0
# for no in arr:
#     sum = sum + no
# print(sum)
# or
# print(sum(arr))

# 3.2 Find the largest element of a list.
# arr = [1, 10, 3, 4]
# largest = arr[0]
# for no in arr:
#     if no > largest:
#         largest = no
# print(largest)
# # or
# print(max(arr))

# 3.3 Take a number as input. Then get the sum of the numbers. If the number is n. Then get
# inpt = int(input('Enter any number:'))
# sum = 0
# for no in range(inpt+1):
#     sum = sum + (no ** 2)
#     print(no)
# print(sum)
