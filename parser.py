#!/usr/bin/env python
import sys, os, stat


boilerplate = '''#!/usr/bin/env python
import sys

#############
##Functions##
#############


##############
##File Input##
##############
path = \'input.in\'
if len(sys.argv)>1: path = sys.argv[1]

try:
    f = open(path, \'r\')
except:
    quit("Error opening file: %s" % path)

data = f.read().splitlines()
f.close()

#Trim extra data from end of file
while data[-1] == '':
    data = data[:-1]
while data[0] == '':
    data = data[1:]

'''


def makeInt(string):
    try:
        return(int(string))
    except:
        return

def dType(aggregate):
    dataType = "int"
    for sample in aggregate:
        try: 
            int(sample)
        except:
            dataType = "float"
            try:
                float(sample)
            except:
                dataType = "str"
                break
    return dataType            

def classify(bunch):
    data = list(bunch)
    alist =  [ line.split(" ") for line in data]
    isList =  max(map(len, alist)) > 1
    if isList:
        print "Data is a list"
    else:
        print "Data not list"

    if not isList:
        aggregate = data
    else:
        aggregate = []
        for line in alist:
            for item in line:
                aggregate.append(item)

    dataType = dType(aggregate)
            

    print "Datatype: %s" % dataType

    if dataType == "str" and isList: 
        isList = False
        print "Ignoring previous assesment: data will not be treated as list"

    return isList, dataType


def t2heuristic(length, data):
    print "Testing for matrices"

    point = 0 
    count = 0

    while point < len(data):
        spec = data[point].split(" ")
        if len(spec) != 2:
            print "Dimension specification has wrong length: ", spec
            return False
        if dType(spec) != "int":
            print "Dimension specification is not an integer: ", spec
            return False

        rows = int(spec[0])
        cols = int(spec[1])
        for x in range(point + 1, point + 1 + rows):
            if len(data[x].split(" ")) != cols:
                print "Row doesn't have specified length: ", data[x]
                return False

        point += rows + 1 
        count += 1

    if count != length:
        print "Failed: wrong number of matrices"
        return False

    if point == len(data):
        print "Passed."
        return True
    else: 
        print "Failed: overshot last length"
        return False


#Default settings which can be changed with flags
PATH = 'input.in'
BACKPAD = 0
TYPE = -1
def interpret(flags):
    if len(flags) > 1 and flags[1][0] != '-':
        global PATH
        PATH = flags[1]
        print "Caught flag, setting PATH = %s" % PATH
    for flag in flags:
        if flag[0] != '-': continue

        #backpad adds specified number of lines padding to end of file
        if len(flag) >= len("-backpad=1") and flag[:9] == '-backpad=':
            global BACKPAD
            BACKPAD = int(flag[9:])
            print "Caught flag, setting BACKPAD = %d" % BACKPAD

        #type forces a particular interpretation
        if len(flag) >= len("-type=1") and flag[:6] == '-type=':
            global TYPE
            TYPE = int(flag[6:])
            print "Caught flag, setting TYPE = %d" % TYPE






interpret(sys.argv)

try: 
    f = open(PATH, 'r')
except:
    quit("Error opening file: %s" % PATH)

data = f.read().splitlines()
f.close()

#Trim extra data from end of file
while data[-1] == '':
    data = data[:-1]
while data[0] == '':
    data = data[1:]

if BACKPAD != 0:
    for x in range(BACKPAD): data.append('')
    boilerplate += "for x in range(%d): data.append('')\n" % BACKPAD


trials = makeInt(data[0])

if trials is None:
    quit("First line is not an integer")
else:
    print "First line integer, assuming number of inputs"
    boilerplate += "trials = int(data[0])\n"

boilerplate += '''
########
##Main##
########
'''


length = (len(data) - 1) / trials

if TYPE == 2 or (t2heuristic(trials, data[1:]) and TYPE == -1):
    print "Interpretting data as matrices, with specified dimensions"
    fodder = []
    rows = int(data[1].split(" ")[0])
    point = 2
    skip = rows + 2
    while point < len(data):
        if point == skip:
            rows = int(data[point].split(" ")[0])
            skip += rows + 1
        else:
            for letter in data[point].split(" "): fodder.append(letter)
        point += 1
    datatype = dType(fodder)
    print "Datatype is %s" % datatype
    boilerplate += "trial = 0\n"
    boilerplate += "blockstart = 2\n"
    boilerplate += "#while trial == 0:\n"
    boilerplate += "while blockstart < len(data):\n"
    boilerplate += "    blockend = blockstart + int(data[blockstart-1].split(\" \")[0])\n"
    boilerplate += "    x = [map(%s, line.split(\" \")) for line in data[blockstart:blockend]]\n" % datatype
    boilerplate += "    blockstart, trial = blockend+1, trial + 1\n\n"
    boilerplate += "    print \"Case #%d: \" %trial\n"
    boilerplate += "    print \"x = \",x\n"

elif TYPE == 1 or (trials*length+1 == len(data) and TYPE == -1):
    print "Data divides evenly into %d trials of length %d" %(trials, length)
    boilerplate += "#for trial in [0]:\n"    
    boilerplate += "for trial in range(trials):\n"
    for line in range(length):
        print line+1
        gather = []
        for trial in range(trials):
            gather.append(data[trial*length + line+1])
        #print gather
        category = classify(gather)
        boilerplate += "    x%d = " % (line+1)
        if not category[0]: #if it's not a list
            boilerplate += "%s(data[trial*%d + %d])\n" % (category[1], length, line+1)
        else: #it is a list
            boilerplate += "map(%s, data[trial*%d + %d].split(\" \"))\n" % (category[1], length, line+1)

    boilerplate += "\n    print \"Case #%d:\" % (trial +1)\n"

    for line in range(length):
        boilerplate += "    print \"x"+str(line+1)+" = \"+str(x"+str(line+1)+")\n"
        
else: 
    quit("Fell through, type not recognized.")


outpath = "parsed." + PATH + ".py"
f = open(outpath, 'w')
f.write(boilerplate)
#set permissions 744
os.chmod(outpath, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)
f.close()
