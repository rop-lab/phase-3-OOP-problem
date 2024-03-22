# Scoreboard Calculator
This Python script calculates and sorts a scoreboard for a competitive eating competition based on the points earned by each participant consuming chicken wings, hamburgers, and hotdogs.

# Functionality
The script consists of two main functions:

calculate_score(participant): This function calculates the score for a given participant based on the number of chicken wings, hamburgers, and hotdogs consumed. It uses the following point system:

Chickenwings: 5 points
Hamburgers: 3 points
Hotdogs: 2 points
create_scoreboard(participants): This function generates a scoreboard for all participants by iterating through the list of participants, calculating the score for each participant using the calculate_score() function, and sorting the scoreboard based on the scores in descending order. If two participants have the same score, they are sorted alphabetically by their names.