# Dependencies
import csv
import os

budget_data_list = []

# Set path for budget_data.csv file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding="UTF-8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    # Get CSV header
    header = next(reader)
    # Test Header
    # print(header)

    pl = []
    months = []

    # Read each row of data after the header
    for row in reader:
        # Calculate the total number of months
        months.append(row[0])

        # Calculate the net total amount of "Profit/Losses" over the entire period
        pl.append(int(row[1]))

    # print(pl)

    # Calculate the revenue change
    rev_change = []

    for i in range(1, len(pl)):
        rev_change.append((int(pl[i]) - int(pl[i - 1])))

    # print(revenue_change)

    # Calculate the Average of the revenue change
    rev_average = sum(rev_change) / len(rev_change)
    # print(round(revenue_average, 2))

    # Find the greatest increase in revenue
    greatest_increase = max(rev_change)
    # Find the greatest decrease in revenue
    greatest_decrease = min(rev_change)

    # Format Number as Currency String
    total = "${:,.2f}".format(sum(pl))
    average_change = "${:,.2f}".format(round(rev_average, 2))
    greatest_inc = "${:,.2f}".format(greatest_increase)
    greatest_dec = "${:,.2f}".format(greatest_decrease)

    # Print the Results
    print("Financial Analysis")

    print("-----------------------------------------------------")

    print(f"Total Months: {str(len(months))}")

    print(f"Total: {total}")

    print(f"Average Change: {average_change}")

    print(f"Greatest Increase in Profits: {str(months[rev_change.index(max(rev_change)) + 1])} {greatest_inc}")

    print(f"Greatest Decrease in Profits: {str(months[rev_change.index(min(rev_change)) + 1])} {greatest_dec}")

    # Create the output text file

    # Specify the file name and directory path
    file_name = "PyBank-Output.txt"
    file_path = os.path.join('analysis', file_name)

    # Creating a file at specified folder
    with open(file_path, 'w') as fp:
        fp.write("Financial Analysis\n")
        fp.write("-----------------------------------------------------\n")
        fp.write(f"Total Months: {str(len(months))}\n")
        fp.write(f"Total: {total}\n")
        fp.write(f"Average Change: {average_change}\n")
        fp.write(f"Greatest Increase in Profits: {str(months[rev_change.index(max(rev_change)) + 1])} {greatest_inc}\n")
        fp.write(f"Greatest Decrease in Profits: {str(months[rev_change.index(min(rev_change)) + 1])} {greatest_dec}\n")
        fp.close()

