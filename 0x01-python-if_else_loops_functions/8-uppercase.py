#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) in range(97, 123)):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
