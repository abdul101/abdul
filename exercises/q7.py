# program gets a input of 7 metropolis, each metropoly will have a name,population,ave annual income and indication if its a capital city
# program will display 7 metropolis, 
#calculate 1) city with least population, 2) city which is NOT a metropolis with highest income 3)capital city with largest population


#initialise variables
less_population =0
less_pop_city=''

big_population =0
big_pop_city=''

most_income_city=''
most_income=0


lst_metropoly=[]
tbl_metropoly=[]
city=''
population=0
income=0
capital=''



# function to check if city is a metropoly, returns True or False
def isMetropoly(capital,population,income):
	if (capital == 'yes') and (population > 100000):
		return True
	else:
		if (population > 200000) and (income > 720000000):
			return True
		else:
			return False
#----end of function			


#main program start - will loop and obtain 7 inputs
for i in range(7):

	lst_metropoly=[]                #initialise empty list

#gets user inputs
	city= raw_input("Name of city: ")
	population= int(raw_input("Population of city: "))
	income=int(raw_input("Annual average income: "))
	capital= raw_input("Is this a capital city- enter 'yes' or 'no': ")

#populates list with user input
        lst_metropoly.append(city)
	lst_metropoly.append(population)
	lst_metropoly.append(income)
	lst_metropoly.append(capital)

#add list to table	
	tbl_metropoly.append(lst_metropoly[:])                  # creates a table with from the list of metropoly
	

#finds the city name of a metropoly with lowest population 	
	if  isMetropoly(capital,population,income):
		if  less_population == 0:				
			less_pop_city = city 		 	     	
			less_population = population
		else:
			if less_population > population:    		#validate initial assumption
				less_pop_city = city
				less_population = population


# finds city which is NOT metropoly with highest income
#NOT metropoly if population < 100 000 or income < 720 000 000


#calls a function to check if metropoly
	if not isMetropoly(capital,population,income):
		if most_income == 0:
			most_income_city = city	    		#assume first city has the highest income
			most_income = income
		else:
			if most_income < income:	    	#validate initial assumption
				most_income = income
				most_income_city = city	



#finds capital city with highest population
	if capital=='yes':
		if  big_population == 0:	
			big_pop_city = city           		# assumes first city has highest population 
			big_population = population
		else:
			if big_population < population:     	#validate initial assumption
				big_pop_city = city
				big_population = population


#output of data
print 'city','\tpopulation','\tincome','\tcapital'		#print headers
for i in range(7):
	for j in range(4):
		print tbl_metropoly[i][j],'\t',			# prints elements in list
	print


# prints city name of metropoly with least population
if less_pop_city == "":
	print 'there is no city which is metropoly with least population'
else:
	print 'the metropolis with less population is: ', less_pop_city

#prints city name which is NOT metropoly with highest income
if most_income != 0:
	print 'the city which is NOT metropoly with highest income: ', most_income_city
else:
	print 'there is no city which is NOT a metropoly highest income'


#prints name of capital city with largest population 
if big_population !=0:
	print 'capital city with the largest population: ', big_pop_city
else:
	print 'there is no capital city metropoly'

	
##  --------- the end -------------			
	




