from operator import index
import os
import csv

csvpath= os.path.join('Resources','budget_data.csv')
csvpath2= os.path.join('analysis' , 'Output.txt')
total_months = 0
total_net = 0
dates=[]
profitloss=[]
previous_profit=0
total_change=0
change_counter=0
changelist=[]




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    

    for row in csvreader:
        total_months = total_months + 1 
        total_net = total_net + int(row[1])
        dates.append(row[0]) 
        profitloss.append(row[1])
        currentprofit=int(row[1])
        if previous_profit!=0:
            change = currentprofit - previous_profit
            changelist.append(change)
            total_change +=change
            change_counter+= 1 
            max_profit=max(changelist)
            min_profit=min(changelist)
        previous_profit=currentprofit 

       






output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${total_change/85}\n"
    f"Greatest Increase in Profits: {max_profit}\n"
    f"Greatest Decrease in Profits: {min_profit}\n")

print(output)
with open(csvpath2,"w+") as txtfile:
    txtfile.write(output) 




