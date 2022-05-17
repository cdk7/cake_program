# def first(word):
#     return word[0]
#
#
# def last(word):
#     return word[-1]
#
#
# def middle(word):
#     return word[1:-1]
#
#
# def is_palindrome(word):
#     if len(word) <= 1:
#         return True
#     if first(word) != last(word):
#         return False
#     return is_palindrome(middle(word))
#
#
# word = input("Enter whatever you want: ")
# print(is_palindrome(word))
# # print(middle('abcde'))
# # print(is_palindrome(word))

# 6.4


def is_power(a, b):
    if a % b == 0 and a / b % b == 0:
        return True
    else:
        return False


a = input("Enter number a: ")
b = input("Enter number b: ")
print(a, type(a), b, type(b))
print(is_power(int(a), int(b)))
