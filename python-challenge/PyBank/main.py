# Import required packages
import csv
import os
import statistics

#paths for read and write file
csvpath= os.path.join("Resources", 'budget_data.csv')


# Placeholders for re-formatted contents
monthlist= [] 
total_vote_number=0
total_value = 0
total_num_month = 0
profit_losses_list = []
monthly_change =[]
# grates_increase_in_profits = max (monthly_change)
# gratest_decrease_in_profits = min(monthly_change)

#read file for data
with open(csvpath, newline='') as bank:
  reader = csv.reader(bank, delimiter=',')

    #there is header, read the head row first
  header = next(bank)
  print(f"Header:{header}") 

  for row in reader:
    total_num_month = total_num_month+1
    total_value = total_value + int(row[1])
    #print(total_value)
    #print(total_num_month)
    profit_losses_list.append(row[1])
    for i in range((len(profit_losses_list))-1):
      change = int(profit_losses_list[i+1]) - int(profit_losses_list[i])
      monthly_change.append(change)
      average_change = statistics.mean(monthly_change)
      #print(average_change)
      greatest_increase = max (monthly_change)
      increase_index =monthly_change.index(greatest_increase)
      print(increase_index)
      greatest_increase_date = monthlist[increase_index]

      greatest_decrease = min(monthly_change)
      decrease_index =monthly_change.index(greatest_decrease)
      greatest_decrease_date = monthlist[decrease_index]
      print(greatest_decrease_date)

    
#path to store file
file_to_output = os.path.join("Financial Analysis.txt")

# # # Generate budget data Analysis Output
output = (
f"Financial Analysis\n"
f"----------------------------------------------\n"
f"Total Months: {total_num_month}\n"
f"Profit_losses Total: ${total_value}\n"
f"Average Change : ${average_change}\n"
f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})\n")

# # # Print all of the results (to terminal)
print(output)

# # # Save the results to analysis text file
with open(bankreport, "w") as txt_file:
  txt_file.write(output)