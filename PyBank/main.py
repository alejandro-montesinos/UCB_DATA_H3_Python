#================================================================
'''
UC Berkeley Extension Data Analytics Program
Homework 3 - Python
Task        : PyBank
Submitted by: Alejandro Montesinos
Date        : March 7, 2019
'''
#-----------------------------------------
#Import Libraries
import os
import csv
#================================================================

#****************************************************************
#Read the CSV file and add the change column

#list to store data
new_date    = []
new_amt     = []
new_change = []
prev_val = 0

#Read file
csvpath = os.path.join('.', 'Resources', 'homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath, newline='') as pyBankData:
    csvreader  = csv.reader(pyBankData, delimiter=',')    
    csv_header = next(csvreader)

    #Loop through observations
    for row in csvreader:   
        new_date.append(row[0])
        new_amt.append(row[1])
        change = int(row[1])-prev_val             #Compute change
        new_change.append(change)                      #Add Change columns to dataset
        prev_val = int(row[1])
        
        
#Save New Dataset for calculation
new_BankData = zip(new_date, new_amt, new_change)                     # Zip lists together
output_file = os.path.join('.', 'Resources',"Clean_pyBank_Data.csv")  # Set variable for output file

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)    
    writer.writerow(["new_date", "new_amt", "new_change"])             # Write the header row
    writer.writerows(new_BankData)                                     # Write in zipped rows
#****************************************************************



#****************************************************************
#Read cleaned data and make the calculations

csvpath = os.path.join('.', 'Resources', 'Clean_pyBank_Data.csv')
with open(csvpath, newline='') as CleanBankData:
    csvreader  = csv.reader(CleanBankData, delimiter=',')    
    csv_header = next(csvreader)

    #Initialize variables
    num_months = 0
    tot_sum    = 0
    tot_chg    = 0
    high_chg   = 0
    low_chg   =  0

    #Loop through observations
    for row in csvreader:        
        num_months += 1                #Add 1 in each loop
        tot_sum    += int(row[1])      #Cummulate total sums
        tot_chg    += int(row[2])      #Cummulate total sums
        
        if int(row[2]) > int(high_chg):
            high_chg  = row[2]
            high_date = row[0]

        if int(row[2]) < int(low_chg):
            low_chg  = row[2]
            low_date = row[0]
            
avg_change =    round((int(tot_chg)-867884)/ (int(num_months)-1),2)       

#Store calculations in variables for output
Header_txt       = "Financial Analysis"
Format_line      = "----------------------------"
Total_Months_txt = "Total Months: " + str(num_months)
Total_Sum_txt    = "Total: $" + str(tot_sum)
AVG_CHG_txt      = "Average Change: "+str(avg_change)
High_CHG_txt     = "Greatest Increase in Profits: " + str(high_date) + " ($"+str(high_chg) +")"
Low_CHG_txt     = "Greatest Decrease in Profits: " + str(low_date) + " ($"+str(low_chg) +")"
#****************************************************************

#****************************************************************
#Print results into terminal and save them in a Text file
L  = [Header_txt,Format_line,Total_Months_txt,Total_Sum_txt, AVG_CHG_txt, High_CHG_txt , Low_CHG_txt]  #Create a list os the values to output
L2 = []                                                          #Create an empty list that is going to be fille in during the loop

for txtt in L:
    print(txtt)              #Print into Temrinal
    L2.append(txtt+" \n")    #Update list with "\n" to be exported into a Textfile

#Save results in a Text File
f = open('./Output/pyBankTable.txt','w')
f.writelines(L2)
f.close()
#****************************************************************


#================================================================
#END OF PROGRAM
#================================================================

