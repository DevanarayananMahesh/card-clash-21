import random
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

def player_move():
    # Choosing a random card

    rank1 = random.choice(ranks)
    value1 = values[rank1]

    # Choosing the second random card

    rank2 = random.choice(ranks)
    value2 = values[rank2]

    if value1 == 11:
        print("you got an Ace, do you want 1 or 11?")
    print(f"You got {rank1} and {rank2}! Your score is {value1+value2}")
    


player_move()