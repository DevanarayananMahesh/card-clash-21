import random
import time

#----------------------------------------------------------   
#                   GLOBAL CONFIG
#---------------------------------------------------------- 

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}




player_score = 0
player_turn = 0
player_status = "none"


bot_score = 0
bot_turn = 0
bot_status = "none"


#----------------------------------------------------------   
# 
#                      PLAYER MOVE
# 
#---------------------------------------------------------- 


def player_move():
    
    global bot_status
    global player_score
    global player_turn  
    global bot_score
    

#----------------------------------------------------------   
#                   HIT/STAY LOGIC
#---------------------------------------------------------- 

    
    if player_turn > 0:
        status = input("\nWould you like to Hit or Stay: ")
        
        while status.lower() != "hit" and status.lower() != "stay":
            status = input("\nPlease type Hit or Stay: ")
        
        if status.lower() == "hit":
            pass
        else:
            
            
            if bot_status == "stay":
                
                print("\nBoth the bot and you selected stay, so the game is over.")
                
                
                if bot_score > player_score:
                    
                    print("\n The bot had a higher score, so it wins")
                    
                elif bot_score < player_score:
                    
                    print("\n You had a higher score than the bot, so you win")
                    
                else:
                    print("\nBoth you and the bot had the same score. It is a tie.")
                return
            
            bot_move()
        
        
    
#----------------------------------------------------------   
#                   RANDOM CARD CHOICE
#---------------------------------------------------------- 

    rank1 = random.choice(ranks)
    value1 = values[rank1]

#----------------------------------------------------------   
#        TIME DELAY EFFECT (idk why i did this lol)
#---------------------------------------------------------- 

    print("\nRolling...")
    time.sleep(1.2)
    


#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value1 == 11:
        value_decide = input("\nYou got an ace, would you like it to be an 11 or 1: ")
        
        while int(value_decide) != 11 and int(value_decide) != 1:

            value_decide = input("\nPlease type 1 or 11: ")
            
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
#                   TIME DELAY EFFECT
#---------------------------------------------------------- 

    print("\nRolling...")
    time.sleep(1.2)
    
    
#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value2 == 11:
        value_decide2 = input("\nYou got an ace, would you like it to be an 11 or 1: ")
        
        while int(value_decide2) != 11 and int(value_decide2) != 1:
            
            value_decide2 = input("\nPlease type 1 or 11: ")
            
        if int(value_decide2) == 11:
            
            value2 = 11
            
        else:
            value2 = 1
    

    player_score = value1+value2 + player_score

#----------------------------------------------------------   
#                EXPRESSING VALUES
#---------------------------------------------------------- 
    
    if player_score > 21:
        
        print(f"\nYou got {rank1} and {rank2}! Your score is {player_score} which exceeds 21.\n You lost.")
        return
    
    elif player_score == 21:
        
        print(f"\nYou got {rank1} and {rank2}! Your score is {player_score},\n therefore you won!")
        return
    
    else:

        #----------------------------------------------------------   
        #                       LOOPING
        #---------------------------------------------------------- 
        
        print(f"\nYou got {rank1} and {rank2}! Your score is {player_score}.")
        
        if player_turn == 0:
            
            player_turn = player_turn + 1
            
            player_move()
        else:
            bot_move()
        
        






#----------------------------------------------------------  
# 
#                   BOT FUNCTION
# 
#---------------------------------------------------------- 










def bot_move():
    
    global bot_score
    global bot_turn

#----------------------------------------------------------   
#                  HIT/STAY LOGIC
#---------------------------------------------------------- 
    
    if bot_turn > 0:
        if bot_score >= 17:
            print("\nThe Bot decided to Stay!")
            bot_status = "stay"
            player_move()
        else:
            bot_status = "hit"
            pass
        
        
        
    
#----------------------------------------------------------   
#                   RANDOM CARD CHOICE
#---------------------------------------------------------- 

    rank1 = random.choice(ranks)
    value1 = values[rank1]

#----------------------------------------------------------   
#                 TIME DELAY EFFECT
#---------------------------------------------------------- 

    print("\nBOT Rolling...")
    time.sleep(1.2)
    


#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value1 == 11:
        
        if bot_score+11 > 21:
            value1 = 1
            
        else:
            value1 = 11
            
            
            
#----------------------------------------------------------   
#               SECOND RANDOM CARD CHOICE
#---------------------------------------------------------- 


    rank2 = random.choice(ranks)
    value2 = values[rank2]
    
    
#----------------------------------------------------------   
#                   TIME DELAY EFFECT
#---------------------------------------------------------- 

    print("\nBOT Rolling...")
    time.sleep(1.2)
    
    
#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 

    if value2 == 11:
        
        if bot_score+11 > 21:
            value2 = 1
            
        else:
            value2 = 11
    

    bot_score = value1+value2 + bot_score

#----------------------------------------------------------   
#                EXPRESSING VALUES
#---------------------------------------------------------- 
    
    if bot_score > 21:
        
        print(f"\nThe bot got {rank1} and {rank2}! It's score is {bot_score} which exceeds 21.\n You won!")
        return
        print("hhahqyusfbqwuebfjhwefwafwefwefwefwef")
    
    elif player_score == 21:
        
        print(f"\nThe bot got {rank1} and {rank2}! The bot's score is {bot_score},\n therefore you lost.")
        return
        print("hhahqyusfbqwuebfjhwefwafwefwefwefwef")
    
    else:

        #----------------------------------------------------------   
        #                   LOOPING LOGIC
        #---------------------------------------------------------- 
        
        print(f"\nThe bot got {rank1} and {rank2}! It's score is {bot_score}.")
        
        if bot_turn == 0:
            
            bot_turn = bot_turn + 1
            
            bot_move()
        else:
            player_move()
        
        


#----------------------------------------------------------   
# 
#                   INIT FUNCTIONS
# 
#---------------------------------------------------------- 

        
player_move()
