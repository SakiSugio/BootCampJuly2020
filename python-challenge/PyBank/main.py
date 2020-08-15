import os
import csv

# Files to load and output 
file_to_load = os.path.join("PyBank/Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_data_analysis.txt")


# Read in the CSV file
with open(file_to_load) as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lists to store data
    total_months = []
    total_profit_loss = []
    profit_loss_change = []

    header = next(csv_reader)

    # Loop through the data
    for row in csv_reader:

        total_months.append(row[0])

        total_profit_loss.append(int(row[1]))

    # Count the total amount of months
    (Total_Months) = len(total_months)

    # Loop through the data of "Profit/Losses"
    for i in range(1,len(total_profit_loss)):
        profit_loss_change.append(int(total_profit_loss[i]) - int(total_profit_loss[i - 1]))

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    average_change = round(sum(profit_loss_change) / len(profit_loss_change),2)

# Get the value and date for greatest increase/decrease
great_increase_amount = max(profit_loss_change)
great_increase_date = total_months[profit_loss_change.index(great_increase_amount) + 1]
great_decrease_amount = min(profit_loss_change)
great_decrease_date = total_months[profit_loss_change.index(great_decrease_amount) + 1]

# Generate analysis output
output = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${sum(total_profit_loss)}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {great_increase_date} (${great_increase_amount})\n"
    f"Greatest Decrease in Profits: {great_decrease_date} (${great_decrease_amount})\n")

# Print all of the results
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)

