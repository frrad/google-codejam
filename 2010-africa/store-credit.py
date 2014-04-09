#!/usr/bin/env python

import sys

def solve(has, credit):
    inventory = list(has)
    inventory.sort()

    a, b = 0, len(inventory)-1

    while inventory[a] + inventory[b] != credit:
        if inventory[a] + inventory[b] > credit:
            b-=1
        elif inventory[a] + inventory[b] < credit:
            a+=1
            
    return inventory[a], inventory[b]

def ans(store, a,b):
    if a !=b:
        first = inventory.index(a)+1
        second = inventory.index(b)+1
    else:
        first = inventory.index(a)
        second = inventory[first:].index(b)
        first +=1
        second += first +1
    
    if first > second:
        return second, first
    else:
        return first, second

f = open(sys.argv[1], 'r')
data = f.read().split("\n")
f.close()

examples = int(data[0])
for x in xrange(examples):
    print "Case #%d:" % (x+1) ,

    credit = int(data[3*x + 1])
    inventory =  map(int,data[3*x + 3].split(" "))

    a,b = solve(inventory, credit)
    print "%d %d" % ans(inventory, a,b)

