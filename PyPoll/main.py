# Dependencies
import csv
import os

votes_counter = 0
candidates_list = []
candidate_name = []
total_votes = []
votes_percent = []

# Set path for budget_data.csv file
csv_path = os.path.join('Resources', 'election_data.csv')

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Get CSV header
    csv_header = next(csv_reader)

    # Loop for getting separate data of the total votes and candidate's name
    for row in csv_reader:
        votes_counter += 1
        candidates_list.append(row[2])

    # Loop for set the unique candidate's names
    for i in set(candidates_list):
        candidate_name.append(i)

        # Counter and allocator of the total number of votes for each candidate
        vc = candidates_list.count(i)
        total_votes.append(vc)

        # Calculate the percentage of votes based on the number of votes of each candidate
        vp = (vc / votes_counter) * 100
        votes_percent.append(vp)

    # Determine the winning number that is the largest number in the list
    winner_number = max(total_votes)

    # Determining the name of the winner of the election based on the index number of the highest number of votes
    winner_name = candidate_name[total_votes.index(winner_number)]

    # Set up the output for terminal
    print("\n")
    print("Election Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {str(votes_counter)}\n")
    print("-------------------------\n")
    print(f"{candidate_name[0]}: {str(round(votes_percent[0], 3))}% ({str(total_votes[0])})\n")
    print(f"{candidate_name[1]}: {str(round(votes_percent[1], 3))}% ({str(total_votes[1])})\n")
    print(f"{candidate_name[2]}: {str(round(votes_percent[2], 3))}% ({str(total_votes[2])})\n")
    print("-------------------------\n")
    print(f"Winner: {winner_name}\n")
    print("-------------------------\n")

    # Create the output Text file PyPoll_Output.txt
    # Specify the file name and directory path
    file_name = "PyPoll-Output.txt"
    file_path = os.path.join('analysis', file_name)

    # Creating a file at specified folder
    with open(file_path, 'w') as fp:
        fp.write("\n")
        fp.write("Election Results\n")
        fp.write("-------------------------\n")
        fp.write(f"Total Votes: {str(votes_counter)}\n")
        fp.write("-------------------------\n")
        fp.write(f"{candidate_name[0]}: {str(round(votes_percent[0], 3))}% ({str(total_votes[0])})\n")
        fp.write(f"{candidate_name[1]}: {str(round(votes_percent[1], 3))}% ({str(total_votes[1])})\n")
        fp.write(f"{candidate_name[2]}: {str(round(votes_percent[2], 3))}% ({str(total_votes[2])})\n")
        fp.write("-------------------------\n")
        fp.write(f"Winner: {winner_name}\n")
        fp.write("-------------------------\n")
        fp.close()

