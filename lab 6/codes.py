# x = 10
# if x>5:
#     print("x is greter than 5")


# x = 10
# if  x>5:
#     print("x is greater than 5")
# elif x ==5:
#    print("x is equal to 5")
# else:
#    print("x is less than 5")
# x=10
# if x>5:
#    print("x is greater than 5")
# else:
#    print("x is not greater than 5")


# age = 35

# if age >= 60:
#     print("You are a senior citizen.")
# else:
#     if age >= 18:
#         print("You are an adult.")
#     else:
#         print("You are a teenager.")


# num = 10

# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive but odd.")
# else:
#     print("The number is not positive.")


# Fruits = ["apple", "banana", "cherry"]
# for fruit in Fruits:
#       print(fruit)


# for x in range(1, 6):
#     if x == 3:
#         break
#     print(x)


# for x in range(1,6):
# 	if x==3:
# 	 continue 
# print(x)


# for x in range(1,6):
#     if x == 3:
#         pass
#     print(x)


# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))


# def add_numbers(a, b):
#     return a + b
# result = add_numbers(3, 5)
# print(result)

# add = lambda x, y: x + y
# print(add(3, 5))  

# def factorial(n):

#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5)) 


# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)  


# def generate_numbers():
#     for i in range(1, 6):
#         yield i
# for number in generate_numbers():
#     print(number)  
# i=1
# while i <= 100:
#     if i%2!=0:
#         print(i)
#     i+=1
    
# i=1
# n= int(input("enter number"))
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

# n=123
# pro=1
# while n!=0:
#     i=n%10
#     pro=pro*i
#     n=n//10
# print(pro)

# n="123"
# for i in range(len(n)):
#     product=

# n=int(input("enter the number"))
# sv=n%10
# print("last number is :",sv)
# string1=str(n)
# sv1=n%10^len(string1)-1
# print("first number is:",sv1)

# n=123
# string1=str(n)
# print("no. of digit is :",len(string1))

n=int(input("enter the number"))
lastnumber=n%10
print("last number is :",lastnumber)
string1=str(n)
firstnumber=n%10^len(string1)-1
print("first number is:",firstnumber)
temp=lastnumber
lastnumber=firstnumber
firstnumber=temp
print("after exchange new first number is:",firstnumber)
print("after exchange new last number is:",lastnumber)