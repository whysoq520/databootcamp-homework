# Import required packages
import csv
import os
import statistics

#paths for read and write file
csvpath= os.path.join("Resources", 'budget_data.csv')


# Placeholders for re-formatted contents
monthlist= [] 
total_value = 0
profit_losses_list = []
monthly_change =[]
grates_increase_in_profits = max (monthly_change)
gratest_decrease_in_profits = min(monthly_change)





#read file for data
with open(csvpath, newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  #there is header, read the head row first
  csv_header = next(csvreader)
  #print(f"Header:{csv_header}")
  #print(csvreader)
  

# print contents
  for row in csvreader:
    # Grab date and store it into a list
    total_value = total_value + (row[1])
    #monthlist.append(row[0])
    monthlist = monthlist + [row[0]]
    #print(monthlist)
# The total number of months included in the dataset
    total_num_month = len(monthlist)
    print(total_num_month)
    #why it print 1-86/ why print all lists? 

# The net total amount of "Profit/Losses" over the entire period
    total_value = total_value + int(row[1])
    #print(total_value)
    profit_losses_list.append(row[1])
    #print(profit_losses_list)
    

#The average of the changes in "Profit/Losses" over the entire period
for i in range((len(profit_losses_list))-1):
  change = profit_losses_list[i+1] - profit_losses_list[i]
  monthly_change.append(change)
  average_change = statistics.mean(monthly_change)


#for i in range(len(profit_losses)):
# #The greatest increase in profits (date and amount) over the entire period
  #greatest_increase = max(profit_losses)
  greatest_increase = max (monthly_change)
  increase_index =monthly_change.index(greatest_increase)
  greatest_increase_date = monthlist[(increase_index+1)]
  

#The greatest decrease in losses (date and amount) over the entire period
  greatest_decrease = min(monthly_change)
  decrease_index =monthly_change.index(greatest_decrease)
  greatest_decrease_date = monthlist[(decrease_index +1)]

#path to store file
  file_to_output = os.path.join("Financial Analysis.txt")

# Generate budget data Analysis Output
output = (
  f"Financial Analysis\n"
  f"-----------------\n"
  f"Total Months: {total_num_month}\n"
  f"Profit_losses Total: ${total_value}\n"
  f"Average Change : ${average_change}\n"
  f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase})\n"
  f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)

  #Financial Analysis

  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)