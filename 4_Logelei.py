#####################################################
# Aufgabe 4: Logelei
#
# leading zeros not allowed (1)
# 2*x must have 5 digits (2)
# each digit 0-9 must occur exacly once (3)
# (1),(2),(3) --> x_min = 12345, x_max 49876

print "x\t2*x"
print "-------------"

x_min, x_max = 12345, 49876

for x in xrange(x_min, x_max + 1):
    y = 2*x
    l = [(x % 10**i) // 10**(i-1) for i in range(5,0,-1)]
    l.extend([(y % 10**i) // 10**(i-1) for i in range(5,0,-1)])

    contains = True
    for index in xrange(0,10):
        contains = contains & (index in l)
    
    if(contains):
        print x, "\t", y
