#!/usr/bin/env python
import sys, math

#############
##Functions##
#############
def works(estimate, a,b):
    paint, r =  int( a),int(b)
    return (4*estimate - 1 + 2*r)**2 <=  1+ 8*paint - 4*r + 4*r**2

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
    x1 = map(int, data[trial*1 + 1].split(" "))
    r, paint = x1[0], x1[1]

    estimate = int(1./4. * (1. - 2.* float(r) + math.sqrt(1. + 8. * float(paint) - 4. * float(r) + 4. * float(r)**2)))

    while not works(estimate, paint, r): estimate -= 1
    while works(estimate,paint,r): estimate += 1

    estimate -= 1
    print "Case #%d: %d" % (trial +1, estimate)

