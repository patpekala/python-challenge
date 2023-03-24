# open and read csv file 
import csv 
import os

csvpath = os.path.join(".", "Resources", "budget_data.csv")
output = os.path.join(".", "analysis", "budget_analysis.txt")

# set variables 
total_months = 0
total_amount = 0 
l_amounts = []
l_dates = []

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        # find total amount of months in dataset
        total_months += 1

        # calculate net total "profit/losses"
        amount = int(row[1])
        total_amount += amount
        l_amounts.append(amount)

        # save dates in a list for later 
        date = row[0]
        l_dates.append(date)

with open(output, "w") as out_file:
    analysis = (
        f"\nFinancial Analysis\n"
        f"-----------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_amount}\n"
    )

    print(analysis)
    out_file.write(analysis)

#compare the values between each two indicies and put them into a new list 

    l_changes = []

    for i in range(len(l_amounts)):
        if (i+1) < len(l_amounts):
            change = int(l_amounts[i+1] - l_amounts[i])
            l_changes.append(change)

    #find average change and greatest increse/decrease in profit 
    average_change = float(sum(l_changes)/len(l_changes))
    max_index = l_changes.index(max(l_changes))
    greatest_date = l_dates[max_index+1]
    min_index = l_changes.index(min(l_changes))
    least_date =l_dates[min_index+1]

    differences = (
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_date} (${max(l_changes)})\n"
        f"Greatest Decrease in Profits: {least_date} (${min(l_changes)})\n"
    )
    print(differences)
    out_file.write(differences)