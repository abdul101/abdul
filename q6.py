# program 

name=''
population=0
isCapital=''
income=0
out_str=''
metropoly = True

name= raw_input("Name of city: ")
population = int(raw_input("Population of city: "))
income=int(raw_input("Annual average income: "))
isCapital = raw_input("Is this a captal city- enter 'yes' or 'no'")


metropoly 

#check if metropoly
if (isCapital == 'yes') and (population > 100000):
	metropoly=True
else:
	if (population > 200000) and (income > 720000000):
		metropoly = True
	else:
		metropoly = False
		out_str = "population less then 200000 or income less then 720000000 "


if metropoly:
	print "this is a metroploy, population > 100 000, annual average income > 720 000 000"
else:
	print "this is NOT a metropoly, ",out_str




