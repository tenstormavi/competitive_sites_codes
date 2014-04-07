from itertools import permutations
t = int(raw_input())
x1 = 0
while t > 0:
    x = raw_input()
    y = raw_input()
    perms = [''.join(p) for p in permutations(x)]
    for i in perms:
        if y.__contains__(i):
    	    x1 = x1 + 1
    if x1 == 0:
    	print "NO"
    else:
    	print "YES"
    x1 = 0
    t = t - 1
