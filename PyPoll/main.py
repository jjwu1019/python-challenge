import pandas as pd
import os
import csv

#import file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
data_file = 'election_data.csv'

data_file_pd = pd.read_csv(data_file)
#print(data_file_pd.head())

#count the instances based on "Voter ID" column in data_file_pd dataframe to find the number of votes and put the results in a list called "total_votes"
total_votes = data_file_pd["Voter ID"].count()
#print(total_votes)

#count the unique names in the "Candidate" column in data_file_pd dataframe to find votes per candidate and put the results in a series called "candidate_count"
candidate_count = data_file_pd["Candidate"].value_counts()
#print(type(candidate_count))

#put the names of candidate into a list called "unique"
unique = data_file_pd["Candidate"].unique()

#convert candidate_count series into a dataframe "candidate_count_df" and copy the index as a new column to get the names
#sort the dataframe in descending order and output the name on top of the dataframe to get the winner's name
candidate_count_df = pd.DataFrame(candidate_count)
sorted_candidate_count_df = candidate_count_df.sort_values("Candidate", ascending=False)
sorted_candidate_count_df['Name'] = sorted_candidate_count_df.index
winner = sorted_candidate_count_df.iloc[0,1]


#output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{unique[0]}: {candidate_count[0]/total_votes*100:.3f}% ({candidate_count[0]})")
print(f"{unique[1]}: {candidate_count[1]/total_votes*100:.3f}% ({candidate_count[1]})")
print(f"{unique[2]}: {candidate_count[2]/total_votes*100:.3f}% ({candidate_count[2]})")
print(f"{unique[3]}: {candidate_count[3]/total_votes*100:.3f}% ({candidate_count[3]})")
print("-------------------------")
print(f"Winner: {winner}")

#output to a text file
output_path = os.path.join("PyPoll.txt")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow("Election Results")
    csvwriter.writerow("-------------------------")
    csvwriter.writerow(f"Total Votes: {total_votes}")
    csvwriter.writerow("-------------------------")
    csvwriter.writerow(f"{unique[0]}: {candidate_count[0]/total_votes*100:.3f}% ({candidate_count[0]})")
    csvwriter.writerow(f"{unique[1]}: {candidate_count[1]/total_votes*100:.3f}% ({candidate_count[1]})")
    csvwriter.writerow(f"{unique[2]}: {candidate_count[2]/total_votes*100:.3f}% ({candidate_count[2]})")
    csvwriter.writerow(f"{unique[3]}: {candidate_count[3]/total_votes*100:.3f}% ({candidate_count[3]})")
    csvwriter.writerow("-------------------------")
    csvwriter.writerow(f"Winner: {winner}")
 