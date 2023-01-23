#!/usr/bin/env python
def simple_function(msg):
    print(msg)


def myfunction():
    print(True)
    return simple_function("Everything is ok")



print(myfunction())
