from functions import center

# Step 1.
# from functions import indent
# res = indent("Hello", 0)
# res = indent("Hi", 5)

strings = input("Please enter one of your favorite strings: ")
screen_width = int(input("Please enter the screen width: "))
res = center(strings, screen_width)
