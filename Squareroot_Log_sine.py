# def add(a,b):
#     c = a+b
#     return c
# ans = add(1,2)
# print(ans)
import math

# def mul(a,b):
#     return a*b
# res = mul(3,"uday ")
# print(res)
# below a,b are parametes of function
# when ever we use return we need to assign it to a variable. IMPORTANT

# we can import modules in 3 ways
#1 as below
# import math
# print(math.pi)
# #  2 as below
# from math import pi
# print(pi)
# #3 as below * imports all functions
# from math import *
# print(pi)

#Recursion = Calling the function inside a function
# import sys
# from platform import python_build
#
# sys.setrecursionlimit(20)
# n = 0
#
# def python():
#     global n
#     n = n+1
#     print("python ",n)
#     python()
#
# python()

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * (factorial(n - 1))
# a = int(input("enter the number "))
# result = factorial(a)
# print(result)



def sqr(n):
   b = math.sqrt(n)
   return b
def log(n):
    c = math.log(n)
    return c
def sine(n):
    d = math.sin(n)
    return d
a = int(input("Enter a number:"))
print(f"Square root: {sqr(a)}")
print(f"Logarithm: {log(a)}")
print(f"sine: {sine(a)}")


