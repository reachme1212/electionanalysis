import csv 
import os
# create variable and assign path to call the file we need to read data from
# add short file path
file_to_load =os.path.join("c:/Users/Sangeetha/Documents/GitHub/electionanalysis/Resources/election_results.csv")
# create variable and assign to path where we write output of analysis
# add short file path
file_to_save =os.path.join("c:/Users/Sangeetha/Documents/GitHub/electionanalysis/Resources/election_analysis.txt")
# create variable to store total number of votes
total_votes=0
# create an empty 'list candidate_options=[candidate_votes={candidate_name1:candidate_votes1}]' we will collect all the candidates name 
candidate_options=[]
county_options=[]
# create a 'dictionary{}' to hold key value pair name:vote count for both candidates and county
candidate_votes={}
county_votes={}
#win_candidate and win_county are string of the candidate name and county names
win_candidate=""
win_count=0
win_percentage=0
win_county_name=""
win_county_votecount=0
win_county_percentage=0
with open(file_to_load) as election_data:
    # Read the file object with the reader function using variable election_data.
    file_reader = csv.reader(election_data)
    #telling to skip header row and go to row 2 
    header=next(file_reader)
    
    #problem in between 29 to 47
    for row in file_reader:
        total_votes=total_votes + 1
         # Skip header start from row 2 counting column from 0 so column 2 is candidate name
        county_name=row[1]
        candidate_name = row[2]
        #line 39 check for candidate names row by row and on 3rd column ,if loop picks the names and add to empty list above 
        # candidate_options
        
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name]=0
        county_votes[county_name] = county_votes[county_name] + 1
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # create dictionary to hold vote count based on candiates name set it to zero 
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    

county_vote_list=[]       
for county_name in county_votes:
    cvotes=county_votes[county_name]
    cvote_percentage= (float(cvotes)/float(total_votes))*100
    county_data=(f'{county_name}: {cvote_percentage:.1f}% ({cvotes:2,})\n')  
    county_vote_list.append(county_data)
    #print(county_data)           
    if( cvotes > win_county_votecount) and (cvote_percentage > win_county_percentage):
        win_county_votecount=cvotes
        win_county_percentage=cvote_percentage
        win_county_name=county_name

candidate_data_list=[]
for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percentage= (float(votes)/float(total_votes))*100
    candidate_data=(f'{candidate_name}: {vote_percentage:.1f}% ({votes:2,})\n')    
    candidate_data_list.append(candidate_data)
    if( votes > win_count) and (vote_percentage > win_percentage):
        win_count=votes
        win_percentage=vote_percentage
        win_candidate=candidate_name

election_results =(f"\nElection Results \n"
    f"--------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"---------------------\n")
print(election_results)
for item in county_vote_list:
    print(item)

largestcountturnout=(f"\n"     
        f"-----------------------------\n"
        f"Largest County Turnout: {win_county_name}\n"
        f"------------------------------\n")
print(largestcountturnout)

winning_candidate_summary = (
    f"\n-------------------------\n"
    f"Winner: {win_candidate}\n"
    f"Winning Vote Count: {win_count:,}\n"  
    f"Winning Percentage: {win_percentage:.2f}%\n"
    f"-------------------------\n")
for item in candidate_data_list:
    print(item)
print(winning_candidate_summary)

with open (file_to_save, "w") as output_file:
    output_file.write(election_results)
    for item in county_vote_list:
        output_file.write(item)
    output_file.write(largestcountturnout)
    for item in candidate_data_list:
        output_file.write(item)
    output_file.write(winning_candidate_summary)
      
output_file.close()
election_data.close()
    