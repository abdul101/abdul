#program converts temperature from degree celsius to fahrenheit
# input a range for degree celsius and output corresponding fahrenheit values



#input degree celsius and converts to float
celsius1=int(raw_input("Temperature in celsius: "))
celsius2=int(raw_input("Temperature in celsius: "))



#print header
print 'C\t','F'


# fahrenheit = (degree celsius * 9/5) + 32, displays output
#checks which number is biggest from input values
if celsius1 > celsius2:
	for x in range(celsius2,celsius1+1):
		print x,'\t',(( x * 9) / 5) + 32	
else:
	for x in range(celsius1,celsius2+1):
		print x,'\t',((x * 9) / 5) + 32

	


