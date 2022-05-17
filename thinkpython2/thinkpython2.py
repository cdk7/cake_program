# 3.1
# def right_justify(string):
#     n = len(string)
#     print(" " * (70 - n) + string)


# 3.2
# def do_twice(func, arg):
#     func(arg)
#     func(arg)


# def print_spam():
#     print('spam')


# def print_twice(arg):
#     print(arg)
#     print(arg)

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
def line1():
    text1 = '+ - - - - '
    print(text1 * 4, end='+')
    print()


def line2():
    text2 = '|         '
    print(text2 * 4, end='|')
    print()


def repeat_2(f):
    f()
    f()


def repeat_4(f):
    repeat_2(f)
    repeat_2(f)


line1()
repeat_4(line2())
line1()
repeat_4(line2())
line1()
