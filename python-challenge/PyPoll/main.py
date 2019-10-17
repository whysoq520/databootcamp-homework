# Import required packages
import csv
import os
import statistics

#paths for read and write file
csvpath= os.path.join("Resources", "election_data.csv")


# Placeholders for re-formatted contents
voter_id_list = []
County_list= []
candidate_list = []

def unique(list):
    unique_list = []     
    for x in list: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
        print(unique_list) 


#read file for data
with open(csvpath, newline='') as election:
  reader = csv.reader(election, delimiter=',')

  #there is header, read the head row first
  header = next(election)
  print(f"Header:{header}") 

  for row in reader:
    # A complete list of candidates who received votes
    voter_id_list = voter_id_list + [row[0]]
    #County_list.append(row[1])
    candidate_list.append(row[2])
    unique(voter_id_list)
    #unique(County_list)
    unique(candidate_list)
   #['Khan', 'Correy', 'Li', "O'Tooley"]



    
 
    # The total number of votes cast      
    total_vote_number = len(voter_id_list)
    #print(voter_id_list)
    print(total_vote_number) #571867
    


  # The total number of votes each candidate won
  #if row[2] not in candidate_list:
      #candidate_list.append(row[2]) 
      #print(candidate_list)
  #actual_canditate_list = ['Khan', 'Correy', 'Li', "O'Tooley"]
  Khan_count = candidate_list.count("Khan")
  Correy_count = candidate_list.count("Correy")
  Li_count = candidate_list.count(actual_candidate_list[2])
  O_Tooley_count = candidate_list.count("O'Tooley")


  

 # The percentage of votes each candidate won
  Khan_percentage = Khan_count/total_vote_number
  Correy_percentage = Correy_count/total_vote_number
  Li_percentage = Li_count / total_vote_number
  O_Tooley_percentage = O_Tooley_count / total_vote_number

# The winner of the election based on popular vote.
winner = max [Khan_count,Li_count,O_Tooley_count,Correy_count]
# Generate Election Results
#output = (
    #f"Election Results\n"
    #f"-----------------\n"
    #f"Total Votes:: {total_vote_number}\n"
    #f"Khan: {Khan_percentage ({Khan_count})
     # Correy: 20.000% (704200)
      #Li: 14.000% (492940)
      #O'Tooley: 3.000% (105630): \n"
    #f"-----------------\n"
    #f"Winner:{winner}: {avg_letter_count}\n"
    #f"-----------------\n"
#output path 
#Election_Results = os.path.join("Election Results.txt")
# Print all of the results (to terminal)
#print(output)

# Save the results to analysis text file
#with open(Election_Results, "a") as txt_file:
    #txt_file.write(output)
