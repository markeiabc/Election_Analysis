# The data we need to retrieve. 
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
print(file_to_load)
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

#Initialize a total vote counter. 

total_votes = 0
largest_county_votes = 0
largest_county_turnout = ""

# Candidate Options
candidate_options = []

#County List
county_options = []

# Declare the open dictionary
candidate_votes = {}

# County dictionary 
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file to provide the requested analysis
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader funtion.
    file_reader = csv.reader(election_data)
    #print(file_reader)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    # For each row in the csv file
    for row in file_reader:
        # We need to add to the total count of votes for the candidates and counties
        total_votes = total_votes + 1

        # Get the candidate name from each row 
        candidate_name = row[2]

        # Get the county name from each row
        county_name = row[1]

        # If the candidate name has not already been added to the list, it will not be added again
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking voter count from 0 
            candidate_votes[candidate_name] = 0
        # This will add a vote to the candidate count 
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
     # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

# Determine the percentage of votes for each county by looping through the counts.
    # 1. Iterate through the county list.
    for county in county_votes:
    # 2. Retrieve vote count of a county.
        cvotes = county_votes[county]
    # 3. Calculate the percentage of votes.
        cvote_percentage = int(cvotes) / int(total_votes) * 100
        #print(f"{county}: received {cvote_percentage:.2F}% of the vote.") 
        county_results = (
            f"{county}: {cvote_percentage:.1f}% ({cvotes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

#Determine largest county turnout 
        if (cvotes > largest_county_votes):
            largest_county_votes = cvotes
            largest_county_turnout = county
    # Print largest county name 
    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)
    
# Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        #print(f"{candidate}: received {vote_percentage:.2F}% of the vote.") 
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
         
         # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
            #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
        #To do: print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)        
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


# Close the file.
election_data.close()
txt_file.close()
       