# How to execute a while statement:
"""
1. Determine whether the condition is true or false.
2. If false, exit the while statement and continue execution at the next statement.
3. If the condition is true, run the body and then go back to step 1.

Infinite loop: loop forever.

"""
import math
#
# def sequence(n):
#     while n != 1:
#         print(n)
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = n * 3 + 1
#
#
# print(sequence(3))


# Newton's method
import math
# x = 5
# a = 7
#
# while True:
#     print(x)
#     y = (x + a/x) / 2
#     if y == x:
#         break
#     x = y


# 7.1
def mysqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def diff(a):
    if mysqrt(a) > math.sqrt(a):
        return mysqrt(a) - math.sqrt(a)
    else:
        return math.sqrt(a) - mysqrt(a)


def test_square_root():
    print("a  mysqrt(a)  math.sqrt(a)  diff \n")
    print("-  ---------  ------------  ---- \n")
    a = 1
    while True:
        print(f"{a}  {mysqrt(a)}  {math.sqrt(a)}  {diff(a)}")
        a = a + 1
        if a == 10:
            break


if __name__ == '__main__':
    test_square_root()

# 7.2
# prompt = eval("math.pi")
# print(prompt)
#
# def eval_loop():
#     print("Enter the variables, or 'done' to quit. ")
#     while True:
#         prompt = input("Enter what you want: ")
#         if prompt != 'done':
#             print(eval(prompt))
#         else:
#             break
#
#
# eval_loop()


# 7.3
# import math
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# def constant_t(m, t):
#     while True:
#         if t == 0:
#             return 1
#         elif t > 0 and isinstance(t, int):
#             return m * constant_t(m, t-1)
#
#
# def estimate_pi():
#     total = 0
#     k = 0
#     post_constant = 2 * math.sqrt(2) / 9801
#     print(post_constant)
#     while True:
#         m = factorial(4 * k) * (1103 + 26390 * k)
#         n = factorial(k)**4 * constant_t(394, 4 * k)
#         total += m / n
#         term = post_constant * m/n
#
#         if abs(term) < 1e-15:
#             break
#         k += 1
#     return 1 / (post_constant * total)
#
#
# print(estimate_pi())
#
# print(math.pi)