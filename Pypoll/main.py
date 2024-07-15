
import os 
import csv


election_file = os.path.join('C:/Users/darji/OneDrive/Desktop/python-challenge/Pypoll/Resources/election_data.csv')


with open(election_file) as file:

    csv_reader = csv.reader(file, delimiter = ",")

    csv_header = next(csv_reader)
 
    votes = 0
    Charles_vote = 0
    Diana_vote = 0
    Raymond_vote = 0
    candidates_dict = {}

    for row in csv_reader:

        votes += 1

        if row[2] == "Charles Casper Stockham":
            Charles_vote += 1
        elif row[2] == "Diana DeGette":
            Diana_vote += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymond_vote += 1

        candidates_dict["Charles Casper Stockham"] = Charles_vote
        candidates_dict["Diana DeGette"] = Diana_vote
        candidates_dict["Raymon Anthony Doane"] = Raymond_vote
   
    max_vote = max(candidates_dict.values())
   
    for name in candidates_dict:
        if max_vote == candidates_dict[name]:
            winner = name

# Output values
output = ("Election Results" + "\n"
          "-------------------------" + "\n"  
          f"Total votes: {votes}" + "\n"
          "-------------------------" + "\n"  
          f"Charles Casper Stockham: {100 * Charles_vote / votes:.3f}% ({Charles_vote})" + "\n"
          f"Diana DeGette: {100 * Diana_vote / votes:.3f}% ({Diana_vote})" + "\n"
          f"Raymon Anthony Doane: {100 * Raymond_vote / votes:.3f}% ({Raymond_vote})" + "\n"
          "-------------------------" + "\n"
          f"Winner: {winner}" + "\n"
          "-------------------------"
         )
    
print(output)

election_final = os.path.join('C:/Users/darji/OneDrive/Desktop/python-challenge/Pypoll/Analysis/Election-results.txt')

with open(election_final, "w") as text_file:
    text_file.write(output)