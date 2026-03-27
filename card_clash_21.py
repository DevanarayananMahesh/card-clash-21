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

game_over = False  # <--THis is proof of how annoying errors are


#----------------------------------------------------------   
# 
#                      PLAYER MOVE
# 
#---------------------------------------------------------- 


"""
This function includes all player moves. It starts by defining 
all variables. It checks the player turn. If the player's turn
(how many turns the player played) is over 0, it asks whether
to hit or stay. A While loop deals with incorrect answers. 
If hit, the code passes, else it checks the bot_status 
(bot's prev move). If it was stay, it checks the scores, and
calls a tie or win. Else, it calls the bot function. 
The function randomly chooses 2 ranks with it's values.
It asks the user for an input of 1 or 11 if one value is an Ace.
A While loop deals with incorrect answers. It then adds the 2
values with the player_score. If this score is more than 21,
You lose, if it is 21, you win, else it prints your rank, values
, and checks your turn. If your turn is 0, it adds 1, and recalls
the function. Otherwise, it calls bot function and ends this function
with a return.

"""

def player_move():
    
    global bot_status
    global player_score
    global player_turn  
    global bot_score
    global game_over

    if game_over:
        return

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

                game_over = True 
                return
                
            else:
                bot_move()
                return  
        
        
    
#----------------------------------------------------------   
#                   RANDOM CARD CHOICE
#---------------------------------------------------------- 

    rank1 = random.choice(ranks)
    value1 = values[rank1]

#----------------------------------------------------------   
#        TIME DELAY EFFECT
#---------------------------------------------------------- 

    print("\nRolling...")
    time.sleep(2)
    

      
#----------------------------------------------------------   
#               SECOND RANDOM CARD CHOICE
#---------------------------------------------------------- 


    rank2 = random.choice(ranks)
    value2 = values[rank2]
    

#----------------------------------------------------------   
#                DECIDING ACE VALUES
#---------------------------------------------------------- 


    if value1 == 11:
        
        value_decide = input(f"\nYou got an ace, your next card will be {rank2}. Would you like it to be an 11 or 1: ")
        
        while int(value_decide) != 11 and int(value_decide) != 1:
            value_decide = input("\nPlease type 1 or 11: ")
            
        if int(value_decide) == 11:
            value1 = 11
        else:
            value1 = 1
            
    if value2 == 11:
        value_decide2 = input(f"\nYou got an ace, your first card is {rank1}. Would you like it to be an 11 or 1: ")
        
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
        game_over = True 
        return
    
    elif player_score == 21:
        
        print(f"\nYou got {rank1} and {rank2}! Your score is {player_score},\n therefore you won!")
        game_over = True  
        return
    
    else:

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


"""
This function codes for the Bot's move. It first defines 
all variables. Then it checks if the game is finished via
a variable. This is set as False if not finished or True if
finished (to avoid repeating problems). If not finished,
the functions shceks if the bot turn is over 0 and under 21.
If so, it checks the bot score. If it is over or equal to
17, the bot's movement is set to stay, and player move is
called. Else, the bot status is hit, and passes the if 
statement. It rolls 2 ranks and values like player move.
If any were an ace, the function does quick math. If
bot_score + 11 + value2 (or value1) > 21, ace value is set to 1.
Else, it is set to 11. The total bot score is updated.
If the bot score is over 21, it stops the function and looses.
If the bot score is 21, it stops the function and prints a win.
If the bot score is under 21, it updates it's turn +1, and calls
player move.
"""

def bot_move():
    
    global bot_score
    global bot_turn
    global bot_status
    global game_over

    if game_over: 
        return

#----------------------------------------------------------   
#                  HIT/STAY LOGIC
#---------------------------------------------------------- 
    
    if bot_turn > 0 and bot_score < 21:
        if bot_score >= 17:
            print("\nThe Bot decided to Stay!")
            bot_status = "stay"
            player_move()
            return  
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

    if value1 == 11:
        if bot_score+value2+11 > 21:
            value1 = 1
        else:
            value1 = 11
            
    if value2 == 11:
        if bot_score+value1+11 > 21:
            value2 = 1
        else:
            value2 = 11
    

    bot_score = value1+value2 + bot_score

#----------------------------------------------------------   
#                EXPRESSING VALUES
#---------------------------------------------------------- 
    
    if bot_score > 21:
        
        print(f"\nThe bot got {rank1} and {rank2}! It's score is {bot_score} which exceeds 21.\n You won!")
        game_over = True 
        return
    
    elif bot_score == 21:
        
        print(f"\nThe bot got {rank1} and {rank2}! The bot's score is {bot_score},\n therefore you lost.")
        game_over = True  
        return
    
    else:

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
