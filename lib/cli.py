from helpers import create_scoreboard

def main():
    participants = [
        {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
        {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
    ]
    
    scoreboard = create_scoreboard(participants)
    print("Scoreboard:")
    for entry in scoreboard:
        print(entry)

if __name__ == "__main__":
    main()
