
from multiprocessing import Queue, Process, process
import multiprocessing


"""flatten a 2D array into one vector"""
def flatten(arr):
    ret = []
    for subarr in arr:
        for elem in subarr:
            ret.append(elem)
    return ret


"""O(logn) time powering function"""
def power(x, n, q):
    j = 1
    v = x
    i = n
    while i>0:
        if i % 2 == 0:
            v = v*v
            i = i/2
        else:
            j = j*v
            i = i-1
    q.put(j) # insert result into queue


def main():
    q = Queue() # new queue
    parr = [[Process(target=power, args=(i,j,q)) for i in range(3,5)] for j in range(3,5)] # compute i to the j for all pairs of 1..5
    parr = flatten(parr) 
    for p in parr: p.start()
    for p in parr: p.join()
    print([q.get() for p in parr])


if __name__ == "__main__":
    main()
