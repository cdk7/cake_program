#  6.1
# def b(z):
#     prod = a(z, z)
#     print(z, prod)
#     return prod
#
#
# def a(x, y):
#     x = x + 1
#     return x * y
#
#
# def c(x, y, z):
#     total = x + y + z
#     square = b(total)**2
#     return square
#
# x = 1
# y = x + 1

# print("x = ", x)
# print("y = ", y+3)
# print("z = ", x+y)
# print('total = ', x+y+3+x+y)

# # rgrs = c(1, 5, 3)
# print(c(x, y+3, x+y))

"""
total = 1 + 5 + 3 = 9
b(9) = a(9,9) = (9+1) * 9 = 90
square = 90*90 = 8100
"""
# 6.2


# def ack(m, n):
#     if m == 0:
#         return n+1
#     elif m > 0 and n == 0:
#         return ack(m-1, 1)
#     elif m > 0 and n > 0:
#         return ack(m-1, ack(m, n-1))
#
#
# print(ack(3, 4))

# 6.3
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


# word = input("Enter whatever you want: ")
# print(is_palindrome(word))
# # print(middle('abcde'))
# # print(is_palindrome(word))
# 6.4


def is_power(a, b):
    if b != 0 and a != 0 \
            and a % b == 0 and a/b % b == 0:
        return True
    elif b == 0 and a == 0:
        return True
    else:
        return False


# 6.5

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
