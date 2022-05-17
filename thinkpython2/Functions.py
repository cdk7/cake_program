# 3.1
# def right_justify(string):
#     n = len(string)
#     print(" " * (70 - n) + string)


# 3.2
# def do_twice(func, arg):
#     func(arg)
#     func(arg)
#
#
# def print_spam():
#     print('spam')
#
#
# def print_twice(arg):
#     print(arg)
#     print(arg)
#
#
# def do_four(func, arg):
#     do_twice(func, arg)
#     do_twice(func, arg)
#
#
# do_twice(print, 'spam')
# print('')
# do_four(print, 'spam')


# 3.3
def line1(n):
    text1 = '+ - - - - '
    print(text1 * n, end='+')
    print()


def line2(n):
    text2 = '|         '
    print(text2 * n, end='|')
    print()


def repeat(f):
    f(n)
    f(n)


def repeat_2(f):
    repeat(f)
    repeat(f)


def row_1(n):
    line1(n)
    repeat_2(line2)


n = int(input("Please enter the columns you need: "))
m = int(input("Please enter the rows you need: "))
for number in range(0, m):
    row_1(n)
line1(n)
