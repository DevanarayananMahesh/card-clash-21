import random

#----------------------------------------------------------   
#                   GLOBAL CONFIG
#---------------------------------------------------------- 

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}



def player_move():
   
#----------------------------------------------------------   
#                   RANDOM CARD CHOICE
#---------------------------------------------------------- 

    rank1 = random.choice(ranks)
    value1 = values[rank1]

#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value1 == 11:
        value_decide = input("You got an ace, would you like it to be an 11 or 1: ")
        
        while int(value_decide) != 11 and int(value_decide) != 1:

            value_decide = input("Please type 1 or 11: ")
            
        if int(value_decide) == 11:
            
            value1 = 11
            
        else:
            value1 = 1
            
            
#----------------------------------------------------------   
#               SECOND RANDOM CARD CHOICE
#---------------------------------------------------------- 


    rank2 = random.choice(ranks)
    value2 = values[rank2]
    
#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value2 == 11:
        value_decide2 = input("You got an ace, would you like it to be an 11 or 1: ")
        
        while int(value_decide2) != 11 and int(value_decide2) != 1:
            
            value_decide2 = input("Please type 1 or 11: ")
            
        if int(value_decide2) == 11:
            
            value2 = 11
            
        else:
            value2 = 1
    

    total_value = value1+value2

#----------------------------------------------------------   
#                EXPRESSING VALUES
#---------------------------------------------------------- 
    
    if total_value > 21:
        
        print(f"You got {rank1} and {rank2}! Your score is {total_value} which exceeds 21. You lost.")
        return
    
    elif total_value == 21:
        
        print(f"You got {rank1} and {rank2}! Your score is {total_value}, therefore you won!")
        return
    
    else:
        
        print(f"You got {rank1} and {rank2}! Your score is {total_value}.")
        status = input("Would you like to Hit or Stay: ")
        
        while status.lower() != "hit" and status.lower() != "stay":
            status = input("Please type Hit or Stay: ")
        
        if status.lower() == "hit":
            player_move()
            # recall function
        else:
            # Changey
            print("Finished Turn")
        
        
player_move()
