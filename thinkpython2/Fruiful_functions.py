# 6.1 Return value
#
# import math

# e = math.exp(1.0)
# height = radius * math.sin(radians)
#
# def area(radius):
#     # # temporary variables can make debugging easier.
#     # a = math.pi * radius**2
#     # return a
#     return math.pi * radius**2

# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x

# dead code:
# As soon as a return statement runs, the functions terminates without executing any subsequent statements.
# Code that appears a return statement, or any other place the flow of execution can never reach.
# import math


# def compare(x, y):
#     if x > y:
#         return(1)
#     elif x == y:
#         return(0)
#     elif x < y:
#         return(-1)
#
#
# print(compare(5, 13))

# Incremental development


# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     # print("dx is ", dx)
#     # print("dy is ", dy)
#     dsquared = dx**2 + dy**2
#     # print("dsquared is ", dsquared)
#     result = math.sqrt(dsquared)
#     # print("Distance is ", result)
#     return result

# The final version of the function doesn't display anything when it runs.
# It only returns a value.
# The print statements wrote are useful for debugging, but once we get the function working, we should remove them.
# Code like that is called scaffolding, it is helpful for building the program but is not part of the final product.
#
# if __name__ == '__main__':
#     distance(1, 2, 5, 5)

"""
Key aspects of incremental development:
1. Start with a working program and make small incremental changes.
    At any point, if there is an error, you should have a good idea where it is.
2. Use variables to hold intermediate values so you can display and check them
3. Once the program is working, you might want to remove some of the scaffolding 
    or consolidated multiple statement into compound expressions, 
    but only if it does not make the program difficult to read.
"""


# Composition
# radius = distance(xc, yc, xp, yp)
# result = area(radius)


# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     area(radius) = math.pi * radius**2
#     result = area(radius)
#     return result


# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


#  Boolean functions
# def is_divisible(x, y):
#     return x % y == 0
#
#     # if x % y == 0:
#     #     return True
#     # else:
#     #     return False
#
#
# x = int(input("Please Enter x = "))
# y = int(input("Please enter y = "))
# # is_divisible(x, y)
# if is_divisible(x, y):
#     print(f"{x} is divisible by {y}. ")
#
# def is_between(x, y, z):
#     return x <= y <= z
#
#
# x = int(input("Please Enter x = "))
# y = int(input("Please enter y = "))
# z = int(input("Please Enter z = "))
# if is_between(x, y, z):
#     print("Correct")


# def is_between(x, y, z):
#     return x <= y <= z
#
#
# x = int(input("Please Enter x = "))
# y = int(input("Please enter y = "))
# z = int(input("Please Enter z = "))
# print(is_between(x, y, z))

# More recursion

#
# def factorial(n):
#     if n >= 0 and isinstance(n, int):
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n-1)
#
#
# print(factorial(4.5))


#  Leap of faith

# def fibonacci(n):
#     if n >= 0 and isinstance(n, int):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#
#
# for n in range(8):
#     print(fibonacci(n))


# Debugging

"""
If a function is not working, there are three possibilities to consider:
1. There is something wrong with arguments the function is getting:
    a precondition is violated
2. There is something wrong with the functions:
    a postcondition is violated
3. There is something wrong with the return value or the way it is being used.
"""


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'return 1')
        return 1
    else:
        result = n * factorial(n-1)
        print(space, 'returning', result)
        return result


factorial(4)