x=2.
s=1.
for k in range(6):
    print "Before iteration %s s equals %s" %(k,s)
    s=0.5*(s+x/s)
print s
