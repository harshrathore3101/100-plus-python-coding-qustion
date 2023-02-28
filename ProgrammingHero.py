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

# 3.4 For a list, find the second largest number in the list.
# Nos = [7,2,43,24,5,6,4,22,1,55,52,54,42,2,77,4,8]
# length = len(Nos)
# high_1 = Nos[0]
# high_2 = Nos[0]
# for no in range(1,length):
#     if Nos[no] > high_1:
#          high_2 = high_1
#          high_1 = Nos[no]
#     elif Nos[no] > high_2:
#          high_2 = Nos[no]
# print(high_2)
# ///////////////////////////////////////////////////////////////////////////////////

# or

# Nos = [7,2,43,24,5,6,4,22,1,68,55,52,54,42,2,4,8]
# Nos.remove(max(Nos))
# print(max(Nos))

# 3.5 For a list, find the second smallest element in the list
# Nos = [7,2,43,24,5,6,4,22,1,68,55,52,54,42,2,4,8,0,0.5]
# Nos.remove(min(Nos))
# print(min(Nos))

# 3.6 For a given string, remove all duplicate characters from that string.
# def remove(str):
#     res = ""
#     for i in str:
#         if i not in res:
#             res += i
#     return res
# str_user = input("Enter a string : ")
# ans=remove(str_user)
# print(ans) 

# str_user = input("Enter a string : ")
# res = ''
# for i in str_user:
#     if i not in res:
#         res+= i
# print(res)

# 4.1 Convert miles to kilometers.
# miles = float(input("Enter distance in miles : "))
# km = miles*1.609344
# print(km)

# 4.2 Take the temperature in degrees Celsius and convert it to Fahrenheit.
# Celsius = float(input("Enter temp :"))
# Fahrenheit = ((Celsius * 9) / 5)+32
# print(Fahrenheit)

# 4.3 Convert a decimal number to binary number.
# /////////////////////////////////////

# 4.4 ////////////////////////////////

# 4.5 ////////////////////////////////

# 6.1 You borrowed $5000 for 2 years with 2% interest per year. Calculate the simple interest to know how much you have to pay?
# price = int(input("Eeter amount : "))
# rate = float(input("Enter intrest rate : "))
# time = float(input("Enter duration : "))
# simple_intrest = (price * rate * time ) / 100
# print(simple_intrest)

# 6.2 Take money borrowed, interest and duration as input. Then, compute the compound interest rate.
# price = int(input("Eeter amount : "))
# rate = float(input("Enter intrest rate : "))
# time = float(input("Enter duration : "))
# compound_intrest = price * ((1+rate/100) ** time)
# print(compound_intrest)

# 6.3 Calculate grade of five subjects.
# print('Enter your marks:')
# sub1=int(input("First subject: "))
# sub2=int(input("Second subject: "))
# sub3=int(input("Third subject: "))
# sub4=int(input("Fourth subject: "))
# sub5=int(input("Fifth subject: "))

# avg = (sub1 + sub2 + sub3 + sub4 + sub5 ) / 5

# if avg >= 90:
#     print("A")
# elif avg >= 80 and avg < 90:
#     print("B")
# elif avg >= 70 and avg < 80:
#     print("C")
# elif avg >= 60 and avg < 70:
#     print("D")
# elif avg < 60:
#     print("E")

# 6.4 Compute gravitational force between two objects.
# F = G m^1m^2/r^2

# m1 = int(input("Enter mass 1 : "))
# m2 = int(input("Enter mass 2 : "))
# distance = int(input("enter distance : "))

# force = (6.673*((10)**-11) * m1 * m2 ) / distance ** 2
# print(force)

# 6.5 Take three sides of a triangle. And then calculate the area of the triangle.
# import math
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
# s = (a + b + c)/2
# area = math.sqrt(s *(s-a) * (s-b) * (s-c))
# print(area)

# 7.1 For a given number, check whether the number is a prime number or not.
# no = int(input("Enter a no. : "))
# for i in range(2,no):
#     if (no % i) == 0:
#         print('Not a prime no.')
#         break
#     else:
#         print("prime ")
#         break

# 7.2 Ask the user to enter a number. Then find all the primes up to that number.

# def is_prime(no):
#     for i in range(2,no):
#         if (no % i) == 0:
#             return False
#         else:
#             return True

# no = int(input("Enter a no. : "))
# primes = []

# for i in range (2, no+1):
#     if is_prime(i) is True:
#         primes.append(i)
# print(primes)

# 7.3 Ask the user to enter a number. Then find all the primes factors for the number.
# no = int(input("Enter a no. : "))
# factor = []

# for i in range(2,no):
#     if (no % i) == 0:
#         factor.append(i)
# print(factor)

# 7.4 Find the smallest prime factor for the given number.
# no = int(input("Enter a no. : "))
# factor = []
# for i in range(2,no):
#     if (no % i) == 0:
#         factor.append(i)
# print(min(factor))

# 8.1 Reverse a string.
# str = input("Enter a string")
# rev = ""
# for i in str:
#     rev = i + rev
# print(rev)

# 8.2 Reverse a string using a stack.
# str = input("Enter a string: ")
# rev = ""
# stack = []
# for i in str:
#     stack.append(i)
# while len(stack) > 0:
#     last = stack.pop()
#     rev = rev + last
# print(rev)

# 8.5 Reverse the word in a sentence.
# usr_input = input("Enter a sentence: ")
# words = usr_input.split()
# words.reverse()
# rev = " ".join(words)
# print(rev)

# 9.1 Check whether the string is a palindrome.
# my_str = input('String to check: ')
# rev_str = my_str[::-1]
# if my_str == rev_str:
#   print("It is palindrome")
# else:
#   print("It is not palindrome")

# 9.2 With a given integral number n, write a program to calculate the sum of cubes.
# user_num = int(input('Enter a number: '))
# sum =0

# for i in range(user_num+1):
#     sum = sum + (i**3)

# print(sum)

# 9.3 Check whether a number is an Armstrong number
# user_num = int(input('Enter a number: '))
# diget = str(user_num)
# sum =0
# order = len(str(user_num))
# temp = user_num
# for i in diget:
#     sum = sum + int(i)**order

# if sum == user_num:
#     print("Is an Armstrong number")
# else:
#   print("Not an Armstrong number")
# print(sum)

# 9.4 Calculate the greatest common divisor (gcd) of two numbers.
# import math
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

#  gcd = 1
# small = min(num1,num2)
# for i in range( 1 , small+1):
#     if (num1 % i == 0) and ( num2 % i == 0):
#         gcd = i

# # or////
# gcd =  math.gcd(num1,num2)
# print(gcd)

#9.5 For two numbers, calculate the least common multiple (LCM).
# import math
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# lcm  = math.lcm(num1,num2)
# print(lcm)

# 11.1 Build a simple guessing game where it will continuously ask the user to enter a number between 1 and 10.
# If the user's guesses matched, the user will score 10 points, and display the score. If the users' guess doesn’t match display the generated number.
# Also, if the user enters “q” then stop the game.

# import random
# print('To stop anytime, enter: q')
# score = 0
# while True:
# 	rand = random.randint(1,10)
# 	inpt = input("enter a number between 1 and 10 : ")
# 	if inpt == 'q' or inpt =="Q":
# 		print("Game over")
# 		break
# 	inpt_no = int(inpt)
# 	if inpt_no == rand:
# 		print("Matched")
# 		score += 10
# 		print('Your new score:', score)
# 	else:
# 		print("doesn’t match")
# 		print(rand)

# 11.2 Build s simple Rock paper Scissor game.

# p1 = input("First player: rock, paper or scissors: ")
# p2 = input("Second Player: rock, paper or scissors: ")

# if p1 == p2:
#     print("It's a tie!")
# elif p1 == 'rock':
#     if p2 == 'paper':
#         print("P2 player wins!")
#     else:
#         print("P1 player wins!")
# elif p1 == 'paper':
#     if p2 == 'scissors':
#         print("P2 player wins!")
#     else:
#         print("P1 player wins!")
# elif p1 == "scissors":
#     if p2 == 'rock':
#         print("P2 player wins!")
#     else:
#         print("P1 player wins!")
# else:
#     print("Invalid input!")

# 11.3 Create a Cows and Bulls game.

# import random
# secret_number = str(random.randint(10, 99))
# print("Guess the number. It contains 2 digits.")
# bull = 0
# cows = 0
# ramining_try = 7
# while ramining_try > 0:
#     player_input = input("Enter ur no. : ")
#     if player_input == secret_number:
#         print("Yooo , You have fucked it")
#         break
#     else:
#         if player_input[0] == secret_number[0]:
#             bull +=1
#         if player_input [1] == secret_number[1]:
#             bull +=1
#         if player_input[0] == secret_number[1]:
#             cows +=1
#         if player_input[1] == secret_number[0]:
#             cows +=1  
#         print("Bull : " , bull)
#         print("Cows : " , cows)

#         ramining_try -= 1
#         if ramining_try < 1:
#             print("Fuck off")
#             break

# print(" final Bull : " , bull)
# print(" final Cows : " , cows)

# 11.4 Create a bulls and cows game for guessing a randomly generated 4 digits number.

# import random
# secret_number = str(random.randint(1000,9999))
# print(secret_number)
# print("Guess the number. It contains 4 digits.")
# ramining_try = 7
# while ramining_try > 0:
#     player_input = input("Enter ur no. : ")
#     if player_input == secret_number:
#         print("Yooo , You have fucked it")
#         break
#     else:
#         bulls_cows = [0,0]
#         for i in range(len(secret_number)):
#             if player_input[i] == secret_number[i]:
#                 bulls_cows[0] += 1
#             if player_input[i] in secret_number:
#                 bulls_cows[1] += 1

#             print("Bulls: ",bulls_cows[0])
#             print("Cows: ",bulls_cows[1])
#         ramining_try -= 1
#         if ramining_try < 1:
#             print("Fuck off")
#             break

# 12.1 Create a simple calculator. That will be able to take user input of two numbers and the operation the user wants to perform.
# def add(n1,n2):
#     return n1 + n2

# def sub(n1,n2):
#     return n1 - n2

# def mult(n1,n2):
#     return n1 * n2

# def div(n1,n2):
#     return n1 / n2

# def modulo(n1,n2):
#     return n1 % n2

# num1 = int(input("Enter first number: "))
# operation = input("What you want to do(+, -, *, /, %):")
# num2 = int(input("Enter second number: "))

# result = 0

# if operation == '+':
#     result = add(num1,num2)
# elif operation == '-':
#     result = sub(num1,num2)
# elif operation == '*':
#     result = mult(num1,num2)
# elif operation == '/':
#     result = div(num1,num2)
# elif operation == '%':
#     result = modulo(num1,num2)

# print(result)

# 12.2 Generate a password. Your password may contain letters in uppercase or lowercase. It also may contain digits or special characters.
# import string
# import random

# pass_len = int(input('How many characters in your password?'))
# all_chr = string.ascii_letters + string.digits + string.printable
# password = ''
# for i in range(pass_len):
#     rand_char = random.choice(all_chr)
#     password += rand_char
# print(password)

# 12.3 Generate a password that has a minimum of one uppercase, one lowercase, one digit, and one special character
# import string
# import random

# pass_len = int(input('How many characters in your password?'))
# all_chr = string.ascii_letters + string.digits + string.printable
# password = ''
# password += random.choice(string.ascii_lowercase)
# password += random.choice(string.ascii_uppercase)
# password += random.choice(string.digits)
# password += random.choice(string.punctuation)
# for i in range(pass_len-4):
#     rand_char = random.choice(all_chr)
#     password += rand_char
# print(password)

# 13.1 Create a simple clock.
# import time

# hours = int(input('Type in the current hour:'))
# minute = int(input('Type in the current minute:'))
# second = int(input('Type in the current second:'))

# def display():
#     print(hours,':',minute,":",second)

# def add():
#     global hours
#     global minute
#     global second

#     second = second+1
#     if second == 60:
#         minute +=1
#         second = 0
#     if minute == 60:
#         hours +=1
#         minute = 0
#     if hours == 24:
#         hours = 0
# print('\n')

# while True:
#     time.sleep(1)
#     add()
#     display()
