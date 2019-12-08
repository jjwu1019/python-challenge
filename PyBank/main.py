import os
import csv

amount_of_month = 0
sum = 0
lists = []
values = []

#open csv file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #header
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    #read the csv file, find amount of months, find the sum of profit/losses, and append content into 2 new list ("lists" and "values") to work with
    for row in csvreader:
        amount_of_month += 1
        sum = sum + int(row[1])
        lists.append(row)
        values.append(row[1])

#using the list "lists" created above, find the greatest inc/dec and store values
greatest_increase = lists[0][1]
greatest_decrease = lists[0][1]

for x in lists:
    if int(x[1]) > int(greatest_increase):
        greatest_increase = x[1]
        inc_month = x[0]
    elif int(x[1]) < int(greatest_decrease):
        greatest_decrease = x[1]
        dec_month = x[0]

#using the list "values", find the values of changes in profit/losses, append them to a new list, and find its average
change_in_value = []

for i in range(1,len(values)):
    change = int(values[i]) - int(values[i-1])
    change_in_value.append(change)

sum_of_average = 0
for z in change_in_value:
    sum_of_average = sum_of_average + z

average_change = sum_of_average / len(change_in_value)

#output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {amount_of_month}")
print(f"Total: {sum}")
print(f"Average Change : {average_change:.2f}")
print(f"Greatest Increase in Profits: {inc_month} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {dec_month} ({greatest_decrease})")

#output to a text file
output_path = os.path.join("PyBank.txt")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
 
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("----------------------------") 
    csvwriter.writerow(f"Total Months: {amount_of_month}") 
    csvwriter.writerow(f"Total: {sum}")
    csvwriter.writerow(f"Average Change : {average_change:.2f}")
    csvwriter.writerow(f"Greatest Increase in Profits: {inc_month} ({greatest_increase})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {dec_month} ({greatest_decrease})")
 