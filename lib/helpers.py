def calculate_score(participant):
    """
    Calculate the score for a participant based on the given food points.
    
    Args:
        participant (dict): Dictionary containing the participant's details.
        
    Returns:
        int: Score calculated based on the food points.
    """
    return participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2

def create_scoreboard(participants):
    """
    Create a scoreboard for the given list of participants.
    
    Args:
        participants (list): List of dictionaries representing participants.
        
    Returns:
        list: List of dictionaries containing 'name' and 'score' properties, sorted by score and then alphabetically by name.
    """
    scoreboard = []
    for participant in participants:
        score = calculate_score(participant)
        scoreboard.append({'name': participant['name'], 'score': score})
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard
