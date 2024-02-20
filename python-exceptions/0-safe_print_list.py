#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    element = 0

    try:
        for i in range(x):
            print(my_list[i], end=' ')
            element += 1

    except IndexError:
        pass

    finally:
        print()

    return element