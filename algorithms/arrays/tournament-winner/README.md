# Tournament Winner

![image](https://user-images.githubusercontent.com/19383145/171064406-7c64f936-d96e-4967-a15b-764dd619844e.png)

![image](https://user-images.githubusercontent.com/19383145/171064473-c72c0df6-9e00-4afe-a1fa-c7ba4717b01a.png)

## Concept Walkthrough

Let's look at an example input

![image](https://user-images.githubusercontent.com/19383145/171064991-c2bda77f-47c6-4f8f-a0bc-e6a722d7c31f.png)

The `competitions` array represents all of the competitions in the tournament. It simply contains pairs that contains two strings. The first string is the name of the home team and the second string is the name of the away team. It's not relevant to call this the home team or the away team. This is how we are going to differentiate which team actually won these competitions. 

The `results` array is going to be the same length as the competitions array. It's going to represent the winner of each of these competitions. 

The indices in the `results` array are going to correspond with the indices in the `competitions` array. 

![image](https://user-images.githubusercontent.com/19383145/171065313-351eb891-01f4-43e8-8100-507509bc354b.png)

When you see a zero in side of the `results` array, this means the away team won the competition. So in the first case, C# is the winner of the competition. The second case, Python is the winner of the competition.

If you see a 1, this means that in the corresponding game, the home team won. So in the 3rd case, Python is the winner. 

We can see that Python won a total of 2 competitions which is the most wins. This means they won the tournament.

You are always going to be given at least two teams. That means you will always have at least one competition. 

The `competitions` array is always going to be the same length of the `results` array. This is because you need a result for every one of the competitions. You can assume you will be given valid input

## Solution Walkthrough

[Solution Code](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/tournament-winner/tournamentWinner.py)

This solution will run in `O(n)` time | `O(k)` space - where n is the number of competitions and k is the number of teams. 

Let's look at how many points each team got in our example

![image](https://user-images.githubusercontent.com/19383145/171066917-e56389ef-25bc-4809-90ba-fa731a9342cd.png)

All we really want to do is look through all the competitions and just keep track of how many points every single team has. 

Once we know all of the points for all of the teams then we can simply go through and figure out which team has the most amount of points then return the name of the team.

To do this, we need to create some kind of data structure that can tell us which team has what number of points. We can either initialize this data structure when we start our algorithm or we can create it as we go through.

We are going to create a data structure called `scores` that is going to be a hash table. The name of the team will be the key and the value will be the team's score. We will initialize it as an empty data structure.

Then we will loop through each of the competitions and figure out what team actually won.

To simulate us looping through the `competitions` list, we can put a green pointer that just tells us which competition we are currently on.

![image](https://user-images.githubusercontent.com/19383145/171067533-bf720cd1-6e84-45cb-88d6-6b97073fe2c5.png)

We want to keep track of the actual competition itself and we want to know the index this competition is at. The reason is we need to access this index in the `results` array so we can figure out what team won. 

We are really going to loop through both the `results` and `competitions` arrays at the exact same time. Then using the value from the results array to figure out which team was the winner. 

Once we figure the winning team, we need to change their score or update their score in our scores data structure. First, we'll check to see if the winning team is already in the scores table. If they are in the scores table, all we need to do is add 3 to their score and update their score to say they won a game. If they are not in the scores table, they have not won a game yet and we need to add them into the table. We can assume that if the team is not in the scores table then their current score is zero. 

So for the first competition in our example, C# is the winner. So we can add the key "C#" and update its value to 3. 

![image](https://user-images.githubusercontent.com/19383145/171068614-313d1581-c714-40b3-a165-97a1ef7d32e2.png)

Then we do the same for the next competition.  

![image](https://user-images.githubusercontent.com/19383145/171068691-f8ed93f4-a50e-48bd-b4f1-99c8f955af63.png)

For the third competition, Python is the winner again. So now we check to see if Python is in the scores table. It is, so all we do is add 3 to the value beside the Python key. Now the value beside the Python key is 6. 

![image](https://user-images.githubusercontent.com/19383145/171069419-11799536-68ee-448a-a9cc-e7885074d178.png)

Now that we've gone through all of our competitions and looked at all of our results, we need to figure out which team had the most number of points. So we loop through the scores table to figure out which team had the best score. 

Let's go over a quick optimization so we do not have to use two for loops. 

We can introduce a new variable that's going to keep track of the highest score that we've currently seen. It will actually keep track of the team that has the highest score. 

We can say `bestTeam = ""`. Whenever a team wins, we will compare the score of the team who just won with the current `bestTeam`. 

At first, our best team is an empty string. So what we should do when we initialize the scores table is add an empty string and say its score is zero. Just so that when we look up this `bestTeam` in our scores table we don't get an index error or something. We will actually have a score returned to us which is really going to be zero.

We have the empty string in our data structure which will give us zero at our first iteration. We can compare it to the score of the team that just won. We will see that the winning team will have the greater score than the empty string which is the current best team. So we update the best team to be the new winning team.  

So let's see what the algorithm will look like when we go through the steps again. 

![image](https://user-images.githubusercontent.com/19383145/171079949-bbd857de-e091-4285-acb9-fe284ee993c8.png)

On the second competition, Python is the winner and its score is 3. So we compare Python's score to the winning team score. The scores are the same so we wont bother updating the `bestTeam` variable. We'll just assume that if Python is the best team, it will get updated later on because there's only ever going to be one winner. 

![image](https://user-images.githubusercontent.com/19383145/171080173-1cc1768e-84dc-4000-bdcb-56b33601e3e7.png)

![image](https://user-images.githubusercontent.com/19383145/171080433-80287b74-ba85-452a-883b-95db7693f902.png)
