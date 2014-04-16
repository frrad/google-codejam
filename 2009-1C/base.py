#!/usr/bin/env python
import sys

#############
##Functions##
#############
def improve(base, threat):
    translate = dict()
    avail = set(range(base))
    
    translate[threat[0]] = 1
    avail.remove(1)
    for let in threat[1:]:
        if let not in translate: 
            translate[let] = min(avail)
            avail.remove(translate[let])

    ans = 0
    exponent = 0
    for let in threat[::-1]:
        ans += base**exponent * translate[let]
        exponent += 1
        
    return ans

def small(base, length):
    return base**(length-1)

##############
##File Input##
##############
path = 'input.in'
if len(sys.argv)>1: path = sys.argv[1]

try:
    f = open(path, 'r')
except:
    quit("Error opening file: %s" % path)

data = f.read().splitlines()
f.close()

#Trim extra data from end of file
while data[-1] == '':
    data = data[:-1]
while data[0] == '':
    data = data[1:]

trials = int(data[0])

########
##Main##
########
#for trial in [0]:
for trial in range(trials):
    alien = str(data[trial*1 + 1])

    print "Case #%d:" % (trial +1),
    
    base = max(len(set(alien)), 2)
    best = improve(base, alien)
    
    while small(base, len(alien)) < best:
        base += 1
        best = min(best, improve(base, alien))

    print best
