# 012
# while True:
#     print(f"Compare the two numbers, and enter 'q' to quit. ")
#     number_1 = input("Enter the first number: ")
#     if number_1 == 'q':
#         break
#     number_2 = input("Enter the second number: ")
#     if number_2 == 'q':
#         break
#
#     if number_1 > number_2:
#         print(f"{number_2}, {number_1}")
#     else:
#         print(f"{number_1}, {number_2}")

# 013
# number = int(input("Enter a number randomly: "))
# if number >= 20:
#     print(f"Too high ")
# else:
#     print(f"Thank you ")

# 014
# number = int(input("Enter a number randomly: "))
# if number > 20 or number < 10:
#     print(f"Incorrect answer ")
# else:
#     print(f"Thank you ")

# 015
# color = input("Please enter your favorite color: ")
# if color in ['red', 'blue', 'green']:
#     print(f"i like {color} too.")
# else:
#     print(f"I don't like {color}, I like red. ")

# color = input("Please enter your favorite color: ")
# if color == 'red' or 'RED' or 'Red':
#     print(f"I like {color} too.")
# else:
#     print(f"I don't like {color}, I like red. ")

# 016
# answer_1 = input("Is it raining now? ")
# if answer_1.lower() == 'yes':
#     answer_2 = input("Is it windy? ")
#     if answer_2.lower() == 'yes':
#         print(f"It is too windy for any umbrella. ")
#     else:
#         print(f"Take an umbrella.")
# else:
#     print("Enjoy your day!")

# 017
# print(f"Answer the question below or enter 'q' to quit. ")

# while True:
#     age = input("How old are you? ")
#     if age == 'q':
#         break
#     elif int(age) >= 18:
#         print(f"You can vote.")
#     elif int(age) == 17:
#         print(f"You can learn to drive.")
#     elif int(age) == 16:
#         print(f"You can buy a lottery ticket.")
#     else:
#         print(f"You can go Trick-or-Treating. ")

# 018

# while True:
#     number = input("Please enter a number, or enter 'q' to quit. ")
#
#     if number == 'q':
#         break
#     elif int(number) < 10:
#         print(f"Too low")
#     elif int(number) > 20:
#         print(f"Too high")
#     else:
#         print(f"Correct")

# 019

while True:
    number = input("Please select one number from 1, 2 or 3: ")
    if number == '1':
        print("Thank you")
    elif number == '2':
        print("Well done")
    elif number == '3':
        print("Correct")
    else:
        print(f"Error message")
        break
