# get total vote cast
# number of candidtaes and names 
# total votes each candidate got 
# % of votes each candidate got 
# winner based on popular vote
# to get date and time use byuild in module import datetime ,print("The time right now is ", now)
# import datetime as dt
# now = dt.datetime.now()
# print("Date and time right now "+str(now) )
# dir(csv)
# Assign a variable for the file to load and the path.
import csv 
import os
#outfile=open(file_to_save, "w")
# outfile.write("hello world")
# outfile.write("\nArapahoe")
# outfile.write("\nDenver")
# outfile.write("\nJefferson")
# outfile.close()
file_to_load =os.path.join("c:/Users/Sangeetha/Documents/GitHub/electionanalysis/Resources/election_results.csv")
file_to_save =os.path.join("c:/Users/Sangeetha/Documents/GitHub/electionanalysis/Resources/election_analysis.txt")
# with open (file_to_load) as election_data:
#     print(election_data)
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    header=next(file_reader)
    print(header)
    # for row in file_reader:
    #     print(row[0])