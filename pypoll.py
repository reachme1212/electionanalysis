# use python builtin import functions csv module to read csv file
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
# create a 'dictionary{}' to hold candidate name:votecount as key value pair that will be inside the list candidate_options
candidate_votes={}
win_candidate=""
win_count=0
win_percentage=0
# open the csv file and assign to a variable called election_data so we can use it as variable not as file path
with open(file_to_load) as election_data:
    # Read the file object with the reader function using variable election_data.
    file_reader = csv.reader(election_data)
    #telling to skip header row and go to row 2 
    header=next(file_reader)
    for row in file_reader:
        total_votes=total_votes + 1
         # Skip header start from row 2 counting column from 0 so column 2 is candidate name
        candidate_name = row[2]
        #line 39 check for candidate names row by row and on 3rd column ,if loop picks the names and add to empty list above 
        # candidate_options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # create dictionary to hold vote count based on candiates name set it to zero 
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    #calculate % of votes for each candidate
    with open (file_to_save, "w") as output_file:
        election_results =(f"\nElection Results\n"
            f"----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------\n")
        print(election_results)
        output_file.write(election_results)
        for candidate_name in candidate_votes:
                votes=candidate_votes[candidate_name]
                vote_percentage= (float(votes)/float(total_votes))*100
                candidate_data=(f'\n{candidate_name}: received {votes:2,} that is {vote_percentage:.2f} % of vote \n')    
                print(candidate_data)
                output_file.write(candidate_data)
                if( votes > win_count) and (vote_percentage > win_percentage):
                    win_count=votes
                    win_percentage=vote_percentage
                    win_candidate=candidate_name
        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {win_candidate}\n"
                f"Winning Vote Count: {win_count:,}\n"  
                f"Winning Percentage: {win_percentage:.2f}%\n"
                f"-------------------------\n")
        print(winning_candidate_summary)
        output_file.write(winning_candidate_summary)    
    output_file.close()
    election_data.close()
    