# The data we need to retrieve. 
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader funtion.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file. 
    for row in file_reader:
        print(row)

# Using the with statement open the file as a text file.  
with open(file_to_save, "w") as txt_file:
# Write three counties to the file. 
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")


# Close the file.
election_data.close()
txt_file.close()

# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

