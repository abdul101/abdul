#program calcultes the Y-value given slope,y-intercept and the x-value given that the function is a straight line
#general formula for straight line is: y =mx + b , m=slope,b=y-intercept,x=x-value,y=y-value
# calulates y-value given m and b for x = 1 to 10

m=0.0
b=0.0


#slope input
m= float(raw_input("enter slope value: "))

#y-intercept input
b= float(raw_input("enter y-intercept value: "))

# printing headers
print "The results for the linear equation Y=mX+b with m=",m," and b=",b, "are:"
#print 'X'.rjust(10),'Y'.rjust(5)
print '\tX','\tY'


# calcultes and displays y for x=1 to 10
for x in range(1,11):
	print '\t',x,'\t',(m * x) + b
	


