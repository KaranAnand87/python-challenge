# First we'll import the os module
import os
# Module for reading CSV files
import csv
import collections
from collections import Counter

# Defining variables
candidates = [ ]
votespercandidate = [ ]
votecount = 0

# Path to collect data from the Resources folder
poll_csvpath = os.path.join("..", "Resources", "election_data.csv")

# Reading of csv files
with open(poll_csvpath, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Reads and stores the header row
    csvheader = next(csvfile)

    # Read through each row of data 
    for row in csvreader:

        #Total number of votes cast
      votecount += 1
      candidates.append(row[2])
    
    #Sorting the list by default ascending order
    sortedlist = sorted(candidates)

    #Counting votes per candidate in most common outcome and appending them
    countcandidate = Counter(sortedlist)
    votespercandidate.append(countcandidate.most_common())

    #Percentage of votes per candidates upto 3 decimal points
    for item in votespercandidate:
        first = format((item[0][1])*100/(sum(countcandidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(countcandidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(countcandidate.values())),'.3f')
        
   
# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votecount}")
print("-------------------------")
print(f"{votespercandidate[0][0][0]}: {first}% ({votespercandidate[0][0][1]})")
print(f"{votespercandidate[0][1][0]}: {second}% ({votespercandidate[0][1][1]})")
print(f"{votespercandidate[0][2][0]}: {third}% ({votespercandidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votespercandidate[0][0][0]}")
print("-------------------------")

#Export a text file with the results
outputfile = os.path.join("..", "Analysis", "polls_data_results.txt")
with open(outputfile, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {votecount}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votespercandidate[0][0][0]}: {first}% ({votespercandidate[0][0][1]})\n")
    outfile.write(f"{votespercandidate[0][1][0]}: {second}% ({votespercandidate[0][1][1]})\n")
    outfile.write(f"{votespercandidate[0][2][0]}: {third}% ({votespercandidate[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votespercandidate[0][0][0]}\n")
    outfile.write("-------------------------\n")