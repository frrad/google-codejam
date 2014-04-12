#!/usr/bin/env python
import sys

def unfilled(board):
    return sum([sum([1 if elt =="." else 0 for elt in line]) for line in board])

def paths(store):
    for i in range(4):
        path = []
        pith = []
        for k in range(4):
            path.append((i,k))
            pith.append((k, i))
        store.append(path)
        store.append(pith)

    store.append([(0,0),(1,1),(2,2),(3,3)])
    store.append([(0,3),(1,2),(2,1),(3,0)])

def won(board, paths):
    for path in paths:
        temp = []
        for stone in path:
            temp.append(board[stone[0]][stone[1]])
        for i, val in enumerate(temp):
            if val == 'T':
                temp[i] = temp[(i+1)%4]

        if temp[0] != "." and temp[0] == temp[1] and temp[1] == temp[2] and temp[2] ==temp[3]:
            return temp[0]

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


for x in range(1): data.append('')
trials = int(data[0])

store = []
paths(store)

for trial in range(trials):


    x1 = str(data[trial*5 + 1])
    x2 = str(data[trial*5 + 2])
    x3 = str(data[trial*5 + 3])
    x4 = str(data[trial*5 + 4])
    x5 = str(data[trial*5 + 5])

    ans =""
    board = [x1,x2,x3,x4]
    winner = won(board,store)
    if winner is None:
        if unfilled(board) > 0: 
            ans = "Game has not completed"
        else:
            ans = "Draw"
    else:
        ans += winner
        ans += " won"

    print "Case #%d: %s" % (trial +1, ans)    

