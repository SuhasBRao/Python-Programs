'''
Program checks the winner of the league given
various match results during the league
Sample inpts:
3
A B 2-1
B C 5-6
C A 2-1
sample output:
6 # indicates the maximum score in league
C # indicates the team which scored maximum points
'''
def winner(inpts):
    team_score_dict = {}
    for i in inpts:
        if i[0] not in team_score_dict: # checks if the team exists in the dictionary
            team_score_dict[i[0]] = 0   # if not adds the team & sets the team score to 0 in dictionart
       

        if i[1] not in team_score_dict:
            team_score_dict[i[1]] = 0
        
        
        if i[2][0] > i[2][1]:           # checks which team won the match
            team_score_dict[i[0]] +=3   # allocates the points for that team 

        if i[2][0] < i[2][1]:
            team_score_dict[i[1]] += 3

        if i[2][0] == i[2][1]:          # if scores are equal then each team in awarded one points
            team_score_dict[i[0]] += 1
            team_score_dict[i[1]] += 1
        
    print(team_score_dict)  # prints the final score table
    teams = list(team_score_dict.keys())
    scores = list(team_score_dict.values())
    print(max(scores))      # prints the highest score
    max_indx = scores.index(max(scores)) 
    print(teams[max_indx])  # team which scored the highest
  

if __name__ =="__main__":   # driver program
    n = int(input())
    inpts = []
    for i in range((n*(n-1)//2)):
        line = list(input().split())
        line[2] = list(map(int,line[2].split('-')))
        #print(line)
        inpts.append(line)
    
    winner(inpts)

