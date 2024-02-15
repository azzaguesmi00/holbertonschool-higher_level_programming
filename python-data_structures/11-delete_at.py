#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    
    if 0 <= idx < len(my_list):
        result_list = my_list[:idx] + my_list[idx + 1:]
        my_list.remove()
        my_list.extend(result_list)
    return my_list
    
   