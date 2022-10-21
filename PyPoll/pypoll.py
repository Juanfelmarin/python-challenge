import os
import csv

csvpath= os.path.join('..','Pypoll/resources','election_data.csv')
csvpath2= os.path.join('analysis' , 'Output.txt')
unique_list=[]
votes=[]


total_vote=0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_vote=total_vote + 1
        unique_list.append(row[2])
        

    candidates=[*set(unique_list)]
    candidates.sort()

    Charles=unique_list.count("Charles Casper Stockham")
    Charles_percent = round ((Charles /total_vote)*100,3)
    Diana=unique_list.count("Diana DeGette")
    Diana_percent = round ((Diana/total_vote)*100,3)
    Raymon=unique_list.count("Raymon Anthony Doane")
    Raymon_percent= round ((Raymon/total_vote)*100,3)

    if Charles_percent> Diana_percent and Charles_percent>Raymon_percent:
        winner="Charles Casper Stockham"
    elif Diana_percent > Charles_percent and Diana_percent>Raymon_percent:
        winner="Diana DeGette"
    elif Raymon_percent > Charles_percent and Raymon_percent>Diana_percent:
        winner="Raymon Anthony Doane"



output = (
    f"Total Votes {total_vote}\n"
    f"Charles Casper Stockham: {Charles_percent}% {Charles}\n"
    f"Diana Degette:{Diana_percent}% {Diana}\n"
    f"Raymon Anthony Doane: {Raymon_percent}% {Raymon}\n"
    f"Winner {winner}"
    )

print(output)
with open(csvpath2,"w+") as txtfile:
    txtfile.write(output)



