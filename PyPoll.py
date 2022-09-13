# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 
#-------------------------------------------------------------------------

#Direct path to the File
#Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# #Open the election results and read the file. 
# with open(file_to_load) as election_data:
# #to do: perform analysis.
#     print(election_data)

#-------------------------------------------------------------------------

#Indirect path to the file
import csv
import os
#Assign  a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save =  os.path.join("analysis", "election_analysis.txt")

#1.initialize a total vote counter
total_votes = 0

candidate_options = []

#1 Declare the empty dictionary.
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file. 
with open(file_to_load) as election_data: 
    # print(election_data)

    # To do: Perform analysis. 
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    # print(headers)

    #Print each row in the CSV file.
    for row in file_reader: 
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n")
        print(election_results, end="")
        #save the final vote count to the text file.
        txt_file.write(election_results)

    # print(candidate_votes)
            # print(row[0]) #to retrieve the first item from each row

    #determine the percentage of votes for each candidate by looping through the counts
    #1. iterate through the candidate list
        for candidate_name in candidate_votes:
            #2. retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3. calculate the percentage of votes 
            vote_percentage = float(votes)/float(total_votes) * 100
            #4. print the candidate name and percentage of votes
            # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

            #to do: print out each candidate's name, vote count, and percentage of
            #votes to the terminal
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate, their voter count, and percentage to the terminal. 
            print(candidate_results)
            #save the candidate results to our text file. 
            txt_file.write(candidate_results)

            #determine winning vote count and candidate
            #determine if the votes is great than the winning count. 
            if (votes > winning_count) and (vote_percentage > winning_percentage): 
                #If true then set winning_count = votes and winning_percentage
                #vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #and, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        #to do: print out the winning candidate, vote count and percentage to the terminal
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n")
        print(winning_candidate_summary)
        #save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)

        #close the file. 
        # election_data.close()

#-------------------------------------------------------------------------

#Create a filename variable to a direct or indirect path to the file.
# file_to_save =  os.path.join("analysis", "election_analysis.txt")
#using the open() function with the "w" mode we will write data to the file. 
    # outfile = open(file_to_save, "w")
    # #write some data to the file.
    # outfile.write("Hello World")
    # #close the file
    # outfile.close()

# #using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file: 
# #     txt_file.write("hello world")
# #write three counties to the file on one line. 
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     # txt_file.write("Arapahoe, Denver, Jefferson") - another way to write them on one line. 

# #write three counties to the file on multiple lines.
#     txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

