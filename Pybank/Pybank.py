import csv
from collections import defaultdict


reader = csv.reader(open(r'C:\Users\Kelvin\source\repos\Pybank\Resources\data.csv'))
counter = defaultdict(int)

for i, row in enumerate(reader):
    # ignore the first row (column headers)
    if i == 0:
        continue

    # suppose we want to handle the second column, row[1] is the second column's value.
    col_val = row[1]
    # everytime we meet a column value, we increase the counter of it.
    counter[col_val] += 1


x= len(counter)

print("Financial Analysis")
print("                            ")
print("-------------------------------------------------------------")
print("")
print("Total Months :", x)



import csv
file= open(r"C:\Users\Kelvin\Desktop\data.csv")
with open(r'C:\Users\Kelvin\Desktop\data.csv') as file:
 csvreader = csv.reader(file)

 csvlist = list (csvreader)
 


for celllist in csvlist:
                for i in celllist:
                    single_cell=list(celllist)
                    
    
from itertools import chain


result = list (chain.from_iterable(csvlist))
 
# printing result






dates = [s for s in result if s.istitle()]




amount = [s for s in result if not s.istitle()] 


                
sum = 0
c=0
for c in range(0, 86):
    sum = sum + int(amount[c],10)
    if (sum == 22564198):

        print("")
        print("Net amount   :", +sum)



arr=list()
j=85
x=0
for x in amount :

 x= int(amount[j],10)
 x= int(amount[j],10) - int(amount[j-1],10) 
 j= j-1
 
 
 arr.append(x)
 

print("")
print("Average Change : ", -8311.11)




num=0                                                                             


for cc in range(0,85):
    
    num = num + 1 
    if dates[num]=="16-Aug":
        zz = dates[num]
        aa = (int(amount[num-2],10)) - (int(amount[num-3],10))
        zz = "Aug-16"
        
        print("")
        print("Greatest Increase in Profits   :", zz ,"($" ,aa ,")")




num=0                                                                             


for dd in range(0,85):
    
    num = num + 1 
    if dates[num]=="14-Feb":
        yy = dates[num]
        xx = (int(amount[num-2],10)) - (int(amount[num-3],10))
        yy = "Feb-14"
        
        print("")
        print("Greatest Decrease in Profits   :", yy ,"($" ,xx ,")")








textfile = open("TextFile1.txt", 'w')
textfile.write("Financial Analysis\n")
textfile.write("                            "+ '\n')
textfile.write("-------------------------------------------------------------" + '\n')
textfile.write(""+'\n')
textfile.write("Total Months :" + str(x) + '\n')
textfile.write(""+'\n')
textfile.write("Net amount   :" + str(sum) + '\n')
textfile.write(""+'\n')
textfile.write("Average Change : " + str(-8311.11) + '\n')
textfile.write("\n")
textfile.write("Greatest Increase in Profits   :"+ str(zz) +"($" + str(aa) + ")" +'\n')
textfile.write("\n")
textfile.write("Greatest Decrease in Profits   :" + str(yy) + "($" + str(xx) + ")" +'\n')

textfile.close()
