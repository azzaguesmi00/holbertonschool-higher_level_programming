#!/usr/bin/python3
def fizzbuzz():
    for numbr in range(1, 101):
        if numbr % 5 == 0 and numbr % 3 != 0:
            print("Buzz ", end="")
        elif numbr % 3 == 0 and numbr % 5 != 0:
            print("Fizz ", end="")
        elif numbr % 5 == 0 and numbr % 3 == 0:
            print("FizzBuzz ", end="")
        else:
            print(f"{numbr}", end=" ")
            