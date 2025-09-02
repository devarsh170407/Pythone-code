# import ex8 as addition
# def add(a,b):
#      result = a+b
#      return result

# a = addition.add(4,5)
# print(a)

#import standard math module 
# import math
# # use math.pi to get value of pi
# print("The value of pi is", math.pi)

# Python import with Renaming
# In Python, we can also import a module by renaming it. For example,
# import module by renaming it
# import math as m
# print(m.pi)

# import only pi from math module
# from math import pi
# print(pi)


# import math
# # print("The value of pi is", pi)


# # print(dir(math))

# help('modules')

# r=5
# a=3.14*r*r
# print(a)

# import math as m 
# # print (math.inf) 
# # print (-math.inf)

# x=10
# y=20
# print(m.pow(x,y), m.sqrt(x), m.trunc(x), m.cos(x), m.sin(x), m.tan(x), m.degrees(x), m.radians(x), m.exp(x), m.log2(x), m.log10(x))


# import math

# def degree_to_radian(degree):
#     radian = degree * (math.pi / 180)
#     return radian

# # Example usage
# degree = 180
# radian = degree_to_radian(degree)
# print(f"{degree} degrees is {radian} radians")

# import math

# def calculate_y(x):
#     y = 6 * x**2 + 4 * math.sin(x)
#     return y

# # Example usage
# x = 2
# y = calculate_y(x)
# print(f"The value of y for x = {x} is {y}")

import math

def evaluate_functions(x):
    f_x = math.cos(2 * x)
    f_prime_x = -2 * math.sin(2 * x)
    f_double_prime_x = -4 * math.cos(2 * x)
    return f_x, f_prime_x, f_double_prime_x

# Example usage
x = math.pi
f_x, f_prime_x, f_double_prime_x = evaluate_functions(x)
print(f"f(x) for x = {x} is {f_x}")
print(f"f'(x) for x = {x} is {f_prime_x}")
print(f"f''(x) for x = {x} is {f_double_prime_x}")