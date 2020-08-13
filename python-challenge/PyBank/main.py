import os
import csv

# Files to load and output 
file_to_load = os.path.join("PyBank/Resources", "budget_data.csv")
#file_to_output = os.path.join("analysis", "paragraph_analysis.txt")

# Read in the CSV file
with open(file_to_load) as csv_file:
    cvs_reader = csv.reader(csv_file)

for row in csv_reader:





#Generate analysis output
output = (
    f"Financial Analysis"
    f"-----------------"
    f"Total Months: {total_months}"
    f"Total: {total_amount}"
    f"Average Change: {average_change}"
    f"Greatest Increase in Profits: {increase_month}"
    f"Greatest Decrease in Profits: {decrease_month}"
)

#Print the results
print(output)