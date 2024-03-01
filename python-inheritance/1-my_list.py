#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):

        """
        Print the list, but sorted 
        """

        sorted_lis = self.copy()
        sorted_lis.sort()
        print(sorted_lis)
