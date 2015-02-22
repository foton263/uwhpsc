def sqrt2(x):
	s=x/2
	kmax=100
	tol=1.e-10
	for k in range(kmax):
	    print "Before iteration %s s equals %20.15f" %(k,s)
	    s0=s
	    s=0.5*(s+x/s)
	    delta_s=abs(s-s0)
	    if (delta_s/x) < tol:
	       break
	print s
