import os
import csv

#path to pull from the resource folder
input_path=os.path.join('Resources','election_data.csv')

#establishing initial lists
Voter=[]
County=[]
Candidate=[]

#convert csv data into list format
with open(input_path,'r') as csv_file:
    reader=csv.reader(csv_file, delimiter=',')
    for n,row in enumerate(reader):
        if not n:#skip header
            continue
        Voter.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    #calculate total number of voters
    Total_votes=(len(Voter))
    #print(Total_votes)
    #Loop through to get summary list of candidates
    Summary_Candidates=[Candidate[0]]
    for x in range(len(Candidate)-1):
        if Candidate[x]!= Candidate[x+1]:
        #If not the same, determine if the name is not already in the summary candidate list
            if Candidate[x+1] not in Summary_Candidates:
                #If not already on the list, add to
                Summary_Candidates.append(Candidate[x+1])
    #print(Summary_Candidates)

    #Calculating total number of votes each candidate won
    #establing a new list to count the votes for each dandidate
    Candidate_votes=[]
    #loops through the Summary Candidate list to initialize 0 votes for each
    for row in Summary_Candidates:
        Candidate_votes.append(0)
    #loops through the original Candidate list from the CSV file
    for x in range(len(Candidate)):
        #loops through the Summary_Candidate list for comparison
        for y in range(len(Summary_Candidates)):
            #Checks if the current name matches 
            if Candidate[x]==Summary_Candidates[y]:
                #If yes, then add one vote for that candidate at y
                Candidate_votes[y]=Candidate_votes[y]+1
    #print(Candidate_votes)

    #Initialize the list for the percentages
    Can_percent=[]

    #Loop through Candidate-votes to alculate the percent for each candidate
    for x in range(len(Candidate_votes)):
        Per_Votes=(Candidate_votes[x]/Total_votes)*100
        Can_percent.append(Per_Votes)
    #print(Can_percent)

    #Determine the winnder, who should have the highest candidate votes
    #loop through Candidate_votes to get the Max
    Max=0
    for x in range(len(Candidate_votes)):
        if Candidate_votes[x]>Max:
            Max=Candidate_votes[x]
            Winner=Summary_Candidates[x]
    #print(Winner)

#Prints the financial analysis to a text file
import sys
sys.stdout=open('Main_PyPoll.txt','w')
#Print out the summary
print("Elections Results")
print("------------------------------------------")
print("Total Votes: " +str(Total_votes))
print("------------------------------------------")
#loops through the length of the summary candidate list for printing the candidatename
#percentage of votes, and the number of votes that candidate received
for x in range(len(Summary_Candidates)):
    print(f'{Summary_Candidates[x]}:  {"{:.3f}".format(Can_percent[x])}% {Candidate_votes[x]}')
print('------------------------------------------')
print(f'Winner: {Winner}')
print('------------------------------------------')

sys.stdout.close()

    
    
