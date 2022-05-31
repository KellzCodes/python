# declare a constant for the value that is used if 
# home team wins tournament
HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # keep track of current best team
    bestTeam = ""
    # hash table
    scores = {bestTeam: 0}

    # get access to the value and index of an element in 
    # competitions array
    for i, competition in enumerate(competitions):
        result = results[i]
        # there are only two values in each competition
        # home team is the first element and away team is second element
        home, away = competition
        # the winning team is home team only if result is 1
        winning = home if result == HOME_TEAM_WON else away
        # update the scores data structure
        updateScores(winning, 3, scores)
        
        if scores[winning] > scores[bestTeam]:
            bestTeam = winning
    return bestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
