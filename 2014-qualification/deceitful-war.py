#!/usr/bin/env python

import sys

def cheat(naomi, ken):
    nscore = 0
    naomi.sort()
    ken.sort()

    while len(naomi) > 0:
        while len(ken) > 0 and   ken[-1] > naomi[-1]:
            ken.pop()
            naomi.pop(0)

        if len(ken) >0 and max(naomi) > max(ken): #should be!
            naomi.pop()
            ken.pop()
            #print "+1 for naomi"
            nscore +=1 

    return nscore

def fair(naomi,ken):
    nscore = 0

    naomi.sort()
    ken.sort()

    while len(naomi) > 0:
        nplay = naomi.pop(0)
        for x in range(len(ken)):
            if ken[x] > nplay:
                ken.pop(x)
                break
        if len(ken) != len(naomi):
            ken.pop(0)
            nscore +=1

    return nscore


path = 'input.in'
if len(sys.argv)>1: path = sys.argv[1]

try:
    f = open(path, 'r')
except:
    quit("Error opening file: %s" % path)

data = f.read().splitlines()
f.close()

length = int(data[0])
for x in range(length):
    naomi = map(float, data[2 + 3*x].split(" "))
    ken = map(float, data[3+ 3*x].split(" "))
    n,k = list(naomi), list(ken)
    print "Case #%d: %d %d" % (x+1, cheat(n,k) , fair(naomi,ken))
