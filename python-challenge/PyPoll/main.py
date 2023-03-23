# open and read csv file 
import csv 
import os

from black import out

# create paths for input and output files 
csvpath = os.path.join(".", "Resources", "election_data.csv")
output = os.path.join(".", "analysis", "election_analysis.txt")

# set variables 
total_votes = 0
l_candidates = []
d_candidate_votes = {}
winning_candidate = ""
winning_votes = 0 

#read csv 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        # find total numbers of votes cast 
        total_votes += 1

        # create a list with candidate names  
        candidate_name = row[2]
        if candidate_name not in l_candidates:
            l_candidates.append(candidate_name)

        # create a dictionary with candidate names and vote counts  
            d_candidate_votes[candidate_name] = 0 
        d_candidate_votes[candidate_name] = d_candidate_votes[candidate_name] + 1 

# write to text file 
with open(output, "w") as out_file:
    results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes} \n"
        f"-----------------------\n"
    )

    print(results)
    out_file.write(results)

    #loop through candiates to assign votes and percentage of total_vote
    for candidate in l_candidates:
        votes = d_candidate_votes.get(candidate)

        percentage = float(votes)/float(total_votes)*100

        # if statements to determine winner 
        if votes > winning_votes:
            winning_votes = votes 
            winning_candidate = candidate

        votes_out = f"{candidate} {percentage:.3f}% ({votes}) \n"
        print(votes_out)
        out_file.write(votes_out)

    winner = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------\n"

    )

    print(winner)
    out_file.write(winner)