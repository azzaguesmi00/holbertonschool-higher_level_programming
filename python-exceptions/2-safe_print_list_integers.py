#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0

    try:
        for i in range(x):
            value = my_list[i]
            print("{:d}".format(value), end=' ')
            integers_printed += 1

    except (ValueError, TypeError, IndexError):
        pass

    finally:
        print()

    return integers_printed
