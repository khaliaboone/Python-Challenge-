import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
total_change = 0
average_change = 0
greatest_increase = {"amount": 0, "date": ""}
greatest_decrease = {"amount": 0, "date": ""}
change_list = []

# Read in the CSV file
try:
    with open(csvpath, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Read the header row
        csv_header = next(csvreader)
        
        # Check if there are no data rows
        try:
            # Initialize with the first row
            first_row = next(csvreader)
            total_months += 1
            net_total += int(first_row[1])
            previous_profit = int(first_row[1])
            
            # Loop through the data
            for row in csvreader:
                # Calculate total months and net total
                total_months += 1
                net_total += int(row[1])

                # Calculate change from current month to previous month
                current_profit = int(row[1])
                change = current_profit - previous_profit
                change_list.append(change)
                total_change += change

                # Update previous profit for next iteration
                previous_profit = current_profit

                # Determine greatest increase and decrease
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = row[0]
                elif change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = row[0]

            # Calculate average change
            if len(change_list) > 0:
                average_change = round(total_change / len(change_list), 2)

            # Generate output summary
            output = (
                f"Financial Analysis\n"
                f"----------------------------\n"
                f"Total Months: {total_months}\n"
                f"Total: ${net_total}\n"
                f"Average Change: ${average_change}\n"
                f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
                f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
            )

            # Print the output to the terminal
            print(output)

            # Export the results to a text file
            output_path = os.path.join("analysis", "financial_analysis.txt")
            with open(output_path, 'w') as txtfile:
                txtfile.write(output)

        except StopIteration:
            print("CSV file is empty or only contains header.")

except FileNotFoundError:
    print(f"Could not find the file at path: {csvpath}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
