
"""
The function can call the others,and it can also can itself.
Recursive: a function that calls itself.
Recursion: the process of executing
"""

# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n-1)
#
#
# def print_n(s, n):
#     if n <= 0:
#         return
#
#     print(s)
#     print_n(s, n-1)
#
#
# if __name__ == '__main__':
#     # countdown(4)
#     print_n("hello", 4)

#  Stack diagrams for recursive functions
#  Infinite recursion: If a recursion never reaches a base case, it goes on making recursive calls forever.


#  5.1
import time
import math
#
# current_time = time.time()
# day = int(current_time // (24 * 3600))
# left_h = current_time % (24 * 3600)
# hour = int(left_h // 3600)
# left_m = left_h % 3600
# minute = int(left_m // 60)
# second = int(left_m % 60)
# print(f"Since epoch, it pas {day} days, {hour} hours, {minute} minutes, and {second} seconds. ")


# 5.2
# def check_fermat(a, b, c, n):
#     if n >= 2 and a^n + b^n == c^n:
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work. ")
#
#
# def rgmts():
#     a = int(input("Enter a: "))
#     b = int(input("enter b: "))
#     c = int(input("enter c: "))
#     n = int(input("enter n: "))
#     check_fermat(a, b, c, n)
#
#
# rgmts()

#  5.3

# def random_triangle():
#     list1 = []
#     for i in range(3):
#         side = int(input("Enter the length of one potential triangle: "))
#         list1.append(side)
#
#     # updated_list = sorted(list1)
#     a = sorted(list1)[0]
#     b = sorted(list1)[1]
#     c = sorted(list1)[2]
#     print(a, b, c)
#     # # print(list1)
#     is_triangle(a, b, c)
#
#
# def is_triangle(a, b, c):
#     if int(a) + int(b) <= int(c):
#         print("No, it can not form a triangle from sticks with the given lengths.")
#     else:
#         print("Yes, you can form a triangle from sticks with the given lengths.")
#
#
# random_triangle()


#  5.4
# def recurse(n, s):
#     if n == 0:
#         print(s)
#     else:
#         recurse(n-1, n+s)
#
#
# recurse(3, 0)
# 3, 0 -> 2, 3
# 2, 3 -> 1, 5
# 1, 5 -> 0, 6

# 5.5
import turtle
#
#
# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length * n)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2 * angle)
#     draw(t, length, n-1)
#     t.lt(angle)
#     t.bk(length * n)
#
# if __name__ == '__main__':
#     args = turtle.Turtle()
#     draw(args, 30, 5)
#

#  5.6
import turtle


def koch(t, m):
    if m < 10:
        t.fd(m)
        return
    n = m / 3
    koch(t, n)
    t.lt(60)
    koch(t, n)
    t.rt(120)
    koch(t, n)
    t.lt(60)
    koch(t, n)


def snowflake(t, m):
    for i in range(3):
        koch(t, m)
        t.rt(120)


if __name__ == "__main__":
    bob = turtle.Turtle()

# bob.pu()
# bob.goto(-150, 90)
# bob.pd()

    snowflake(bob, 300)
    # turtle.mainloop()

"""

def koch(t, n):
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)
        

args = turtle.Turtle()

args.pu()
args.goto(-150, 90)
args.pd()

snowflake(args, 300)
turtle.mainloop()

"""