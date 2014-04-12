#!/usr/bin/env python
import sys, os, stat


boilerplate = '''#!/usr/bin/env python
import sys

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
            

    print "Datatype: %s" % dataType

    if dataType == "str" and isList: 
        isList = False
        print "Ignoring previous assesment: data will not be treated as list"

    return isList, dataType

#Default settings which can be changed with flags
PATH = 'input.in'
BACKPAD = 0
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

length = (len(data) - 1) / trials

if trials*length+1 == len(data):
    print "Data divides evenly into %d trials of length %d" %(trials, length)
    boilerplate += "#for trial in [0]:\n"    
    boilerplate += "for trial in range(trials):\n"
    boilerplate += "    print \"Case #%d:\" % (trial +1)\n\n"
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

    boilerplate += "\n"

    for line in range(length):
        boilerplate += "    print \"x"+str(line+1)+" = \"+str(x"+str(line+1)+")\n"
        
        
else:
    quit("Data doesn't divide evenly into trials")



outpath = "parsed." + PATH + ".py"
f = open(outpath, 'w')
f.write(boilerplate)
#set permissions 744
os.chmod(outpath, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)
f.close()
