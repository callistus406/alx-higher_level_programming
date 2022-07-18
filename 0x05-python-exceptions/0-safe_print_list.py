#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for idx in range(x):
        try:
            print(my_list[idx], end='')
            result +=1
        except Exception as  error:
            break

    print("")
    return result
