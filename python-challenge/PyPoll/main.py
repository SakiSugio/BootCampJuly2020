import os
import csv

# Files to load and output 
file_to_load = os.path.join("PyPoll/Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_data.csv .txt")

# Create variables
total_votes = 0
candidate_list = {}
candidate_vote = {}

# # Read in the CSV file
with open(file_to_load) as csv_file: 
    csvreader = csv.reader(csv_file, delimiter = ",")

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] in candidate_list:
            candidate_list[row[2]] += 1
        else :
            candidate_list[row[2]] = 1
    # Find the winner
    winner = max(candidate_list, key = candidate_list.get)

    for key in candidate_list.keys():
        # Calculate the percentage of votes 
        voter = []
        voter.append(candidate_list[key]/total_votes)

        voter.append(candidate_list[key])
        candidate_vote[key] = voter

# Generate analysis output
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
for t in candidate_vote:
    print(f"{t}: {'{:.3%}'.format(candidate_vote[t][0])} ({candidate_vote[t][1]})")
print(f"------------------------")
print(f"Winner: {winner}")
print(f"------------------------")

# Save the results to analysis text file
txt_file = open(file_to_output, "w") 
txt_file.write(f"\nElection Results\n")
txt_file.write(f"------------------------\n")
txt_file.write(f"Total Votes:{total_votes}\n")
txt_file.write(f"------------------------\n")
for t in candidate_vote:
    txt_file.write(f"{t}:  {'{:.3%}'.format(candidate_vote[t][0])} ({candidate_vote[t][1]})\n")
txt_file.write(f"------------------------\n")
txt_file.write(f"Winner: {winner} \n")
txt_file.write(f"------------------------\n")
