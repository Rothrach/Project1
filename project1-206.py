# how to make it save on the git
	#git add [filename]
	#git commit -m "[message]"
	#git push
import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv



def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	infile=open(file,"r")
	reader= csv.reader(infile)
	headers=reader.__next__()
	lists=[]
	for line in reader:
		data={}
		data[headers[0]]=line[0]
		data[headers[1]]=line[1]
		data[headers[2]]=line[2]
		data[headers[3]]=line[3]
		data[headers[4]]=line[4]
		if data not in lists:
			lists.append(data)
	#print(lists)
	return lists




def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sortedkeys=sorted(data,key=lambda k:k[col])
	#print (sortedkeys)
	firstkey=sortedkeys[0]
	firstname=firstkey["First"]
	lastname=firstkey["Last"]
	return firstname + " " + lastname



def classSizes(data):
# Create a histogram
# # Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	fresh_acum=0
	sophmore_acum=0
	junior_acum=0
	seniors_acum=0
	for dictionary in data:
		gettingclass=dictionary["Class"]
		if gettingclass=="Freshman":
			fresh_acum+=1
		elif gettingclass=="Sophomore":
			sophmore_acum+=1
		elif gettingclass=="Junior":
			junior_acum+=1
		elif gettingclass=="Senior":
			seniors_acum+=1
	list_numbers=[('Senior', seniors_acum), ('Junior', junior_acum), ('Freshman', fresh_acum), ('Sophomore', sophmore_acum)]
	return sorted(list_numbers,key=lambda k:k[1],reverse=True)

def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	dict={}
	for dictionary in a:
		gettingdob=dictionary["DOB"]
		spliting=gettingdob.split("/")
		dict[spliting[0]]=dict.get(spliting[0],0)+1
	#print(dict)

	return int(sorted(dict,key=dict.get,reverse=True)[0]) # now we have dictionary not tuples only wanted the first number in list



def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	mywritefile=open(fileName,"w")
	sortedkeys=sorted(a,key=lambda k:k[col])
	for student in sortedkeys:
		firstname=student["First"]
		lastname=student["Last"]
		email=student["Email"]
		mywritefile.write(firstname + "," + lastname + "," + email + "\n")
	mywritefile.close()


def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	dict={}
	ages = 0
	numberpeople = 0
	for dictionary in a:
		gettingdob=dictionary["DOB"]
		spliting=gettingdob.split("/")
		theredates=date(int(spliting[2]),int(spliting[0]),int(spliting[1]))
		age=date.today()-theredates
		age=round(age.days/365)
		ages+=age
		numberpeople+=1
	return(round(ages/numberpeople))
		#print(age)
		#convert it to years google python date time covert dates to years
		#take that number and round it to nearest year
		#for each student you want to get that age accum it to a list then
		#once have it at end of for loop fine the average of list

	#return sorted(dict,key=dict.get,reverse=True)[0] # now we have dictionary not tuples only wanted the first number in list



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
