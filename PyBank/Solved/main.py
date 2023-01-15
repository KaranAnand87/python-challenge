# First we'll import the os module
import os
# Module for reading CSV files
import csv

#Defining variables
months = [ ]
plchanges = [ ]
monthcount = 0
netpl = 0
lmpl=0
cmpl=0
plchange = 0

# Path to collect data from the Resources folder
bank_csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Reading of CSV files
with open(bank_csvpath, encoding='utf') as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ",")
  #Reads and stores the header row
  csvheader = next(csvfile)
  

  # Read through each row of data 
  for row in csvreader:
      #Total number of months included in the dataset
      monthcount += 1

      #The net total amount of "Profit/Losses" over the entire period
      cmpl=int(row[1])
      netpl += cmpl

      if (monthcount == 1):
          lmpl = cmpl
          continue
    
      else:
          #Compute change in Profit/Loss
          plchange = cmpl - lmpl

          #Append each month to the months
          months.append(row[0])

          #Append each profit/loss change to plchange
          plchanges.append(plchange)

          lmpl = cmpl

  #The sum of the changes in "Profit/Losses" over the entire period
  sumpl = sum(plchanges)

  #The average of the changes in "Profit/Losses" over the entire period
  averagepl = round(sumpl/(monthcount-1),2)

  #The greatest increase in profits (date and amount) over the entire period
  highestchange = max(plchanges)
  highestmonth = plchanges.index(highestchange)
  bestmonth = months[highestmonth]

  #The greatest decrease in profits (date and amount) over the entire period
  lowestchange = min(plchanges)
  lowestmonth = plchanges.index(lowestchange)
  worstmonth = months[lowestmonth]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {monthcount}")
print(f"Total:  ${netpl}")
print(f"Average Change:  ${averagepl}")
print(f"Greatest Increase in Profits:  {bestmonth} (${highestchange})")
print(f"Greatest Decrease in Profits:  {worstmonth} (${lowestchange})")

# Exporting a text file with the results
analysis_file = os.path.join('..', 'Analysis', 'analysis_data.txt')
with open(analysis_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {monthcount}\n")
    outfile.write(f"Total:  ${netpl}\n")
    outfile.write(f"Average Change:  ${averagepl}\n")
    outfile.write(f"Greatest Increase in Profits:  {bestmonth} (${highestchange})\n")
    outfile.write(f"Greatest Decrease in Profits:  {worstmonth} (${lowestchange})\n")