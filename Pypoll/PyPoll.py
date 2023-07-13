
import csv
file= open(r"C:\Users\Kelvin\source\repos\Pypoll\Resources\poll.csv")
with open(r"C:\Users\Kelvin\source\repos\Pypoll\Resources\poll.csv") as file:
 csvreader = csv.reader(file)
 
 print("Election Results")
 print("---------------------------------------------------------------")
 

 csvlist = list (csvreader)
 
 

 for celllist in csvlist:
                for i in celllist:
                    single_cell=list(celllist)
                    
    
from itertools import chain
import re 
 

 

result = list (chain.from_iterable(csvlist))



Ballot_ID = [s for s in result if s.isnumeric()]

count=0
for i in Ballot_ID:
    count = count + 1
    
    if count == len(Ballot_ID):
        print("")
        print("Total number of votes :" ,count)

print("")
print("--------------------------------------------------------------")

charles_count = result.count("Charles Casper Stockham")
ca=((charles_count/count)*100)
print("")
print("Charles Casper Stockham :",round(ca,3),"%" , "(",charles_count,")")



diana_count = result.count("Diana DeGette")
da = ((diana_count/count)*100)
print("")
print("Diana DeGette :",round(da,3),"%" , "(",diana_count,")")



raymon_count = result.count("Raymon Anthony Doane")
ra = ((raymon_count/count)*100)
print("")
print("Raymon Anthony Doane :",round(ra,3),"%" , "(",raymon_count,")")


print("")
print("")
print("-------------------------------------------------")


if raymon_count >= diana_count and raymon_count >= charles_count:
        print("Winner: Raymon Anthony Doane")
elif charles_count >= raymon_count and charles_count >= diana_count:
        print("Winner: Charles Casper Stockham")
else:
        print("Winner: Diana Gelette")


print("-----------------------------------------------------")





textfile = open("TextFile2.txt", 'w')
textfile.write("Election Results\n")
textfile.write("                            "+ '\n')
textfile.write("-------------------------------------------------------------" + '\n')
textfile.write(""+'\n')
textfile.write("Total number of votes :" + str(count) + '\n')
textfile.write(""+'\n')
textfile.write("-------------------------------------------------------------" + '\n')
textfile.write("Charles Casper Stockham :" + str(round(ca,3)) + "%" + "(" + str(charles_count)+ ")" + '\n')
textfile.write(""+'\n')
textfile.write("Diana DeGette :" + str(round(da,3)) + "%" + "("+ str(diana_count) +")" + '\n')
textfile.write("\n")
textfile.write("Raymon Anthony Doane :" + str(round(ra,3)) + "%" + "(" + str(raymon_count) + ")" + '\n')
textfile.write("\n")
textfile.write("\n")
textfile.write("-------------------------------------------------------------" + '\n')
textfile.write("Winner: Diana Gelette" + '\n')
textfile.write("-------------------------------------------------------------" + '\n')
textfile.close()

   
















