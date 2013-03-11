#program calcultes the Y-value given slope,y-intercept and the x-value given that the function is a straight line
#general formulau for straight line is: y =mx + b , m=slope,b=y-intercept,x=x-value,y=y-value
m=0.0
b=0.0
x=0.0

#slope input
m= float(raw_input("enter slope value: "))

#y-intercept input
b= float(raw_input("enter y-intercept value: "))

#x-value input
x= float(raw_input("enter x-value: "))

#calculate and display y-value
print "the y-value is: ", (m * x) + b



