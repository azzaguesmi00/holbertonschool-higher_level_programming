#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        element = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        element = None
    finally:
        print("Inside result: {}".format(element))
    return element
