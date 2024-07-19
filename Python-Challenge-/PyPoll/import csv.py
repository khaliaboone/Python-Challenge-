import csv

# Full absolute path to the CSV file
file_path = "C:/Users/000154302/OneDrive/dataviz2024/UNC-VIRT-DATA-PT-06-2024-U-LOLC/Homework/Python-Challenge-/PyPoll/election_data.csv"

try:
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Read the CSV file
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        next(csvreader)

        # Iterate through each row in the CSV
        for row in csvreader:
            # Count total votes
            total_votes += 1

            # Get the candidate name from the row
            candidate_name = row[2]

            # Add the candidate to the dictionary if not already present
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0

            # Increment the candidate's vote count
            candidate_votes[candidate_name] += 1

    # Determine the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

except FileNotFoundError:
    print(f"ERROR: File '{file_path}' not found. Please check the file path.")
