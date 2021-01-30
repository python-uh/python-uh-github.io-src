#! /usr/bin/env python3
""" Some slow computations. """

from time import time
from timeit import timeit
from random import shuffle


def bench(funct):
    def helper(*args):
        start = time()
        res = funct(*args)
        stop = time()
        secs = stop - start
        print(f"execution took {secs:.4} seconds")
        return res
    return helper


def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

def tim_sort(data):
    data.sort()


def main():
    lst = list(range(5000))
    shuffle(lst)
    bubble_sort(list(lst))
    tim_sort(list(lst))

    env = globals()
    env["lst"] = lst
    secs= timeit("tim_sort(list(lst))", number=10, globals=env)
    print(f"execution took {secs} seconds")


if __name__ == "__main__":
    main()
    
