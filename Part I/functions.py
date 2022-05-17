def center(strings, screen_width):
    spaces = (screen_width - len(strings)) / 2
    for i in range(0, int(spaces)):
        print(' ', end='')
    print(f"{strings}")
    return()


def indent(strings, spaces):
    for i in range(0, int(spaces)):
        print(' ', end='')
    print(f"{strings}")
    return()
