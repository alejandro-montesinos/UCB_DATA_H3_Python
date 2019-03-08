#================================================================
'''
UC Berkeley Extension Data Analytics Program
Homework 3 - Python
Task        : PyPoll
Submitted by: Alejandro Montesinos
Date        : March 7, 2019
'''
#-----------------------------------------
#Import Libraries
import os
import csv
import pandas as pd     #Use pandas because running time with CSV was too long!
#================================================================

#****************************************************************
#Read in CSV file and print first 5 rows
poll_data = "Resources/homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
poll_pd = pd.read_csv(poll_data)
poll_pd.head()
#****************************************************************


#****************************************************************
#Count votes per candidate and save it into a new Data Frame
candidate_counts = poll_pd["Candidate"].value_counts()
candidate_counts_df = pd.DataFrame(candidate_counts)
candidate_counts_df = candidate_counts_df.rename(columns={"Candidate":"Votes"})
total_votes = candidate_counts_df["Votes"].sum()
percent = round(((candidate_counts_df["Votes"]/total_votes)*100),2)
candidate_counts_df["Percent"] = percent
candidate_counts_df
#****************************************************************

#****************************************************************
#Compute all the data we need
Header_txt       = "Election Results"
Format_line      = "----------------------------"
Total_Sum_txt    = "Total Votes: " + str(total_votes)
khan_votes   = "Khan: "+ str(candidate_counts_df.loc["Khan", "Percent"])+ "% (" + str(candidate_counts_df.loc["Khan", "Votes"]) + ")"
correy_votes = "Correy: "+ str(candidate_counts_df.loc["Correy", "Percent"])+ "% (" + str(candidate_counts_df.loc["Correy", "Votes"]) + ")"
li_votes = "Li: "+ str(candidate_counts_df.loc["Li", "Percent"])+ "% (" + str(candidate_counts_df.loc["Li", "Votes"]) + ")"
otooley_votes = "O'Tooley: "+ str(candidate_counts_df.loc["O'Tooley", "Percent"])+ "% (" + str(candidate_counts_df.loc["O'Tooley", "Votes"]) + ")"
winner = "Winner: Khan"
#****************************************************************


#****************************************************************
#Print results into terminal and save them in a Text file
L  = [Header_txt,Format_line,Total_Sum_txt,Format_line, khan_votes,correy_votes,li_votes,otooley_votes,Format_line,winner,Format_line]  #Create a list os the values to output
L2 = []                                                          #Create an empty list that is going to be fille in during the loop


for txtt in L:
    print(txtt)              #Print into Temrinal
    L2.append(txtt+" \n")    #Update list with "\n" to be exported into a Textfile

#Save results in a Text File
f = open('./Output/pyPollTable.txt','w')
f.writelines(L2)
f.close()
#****************************************************************


#================================================================
#END OF FILE
#================================================================