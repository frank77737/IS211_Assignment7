import random
random.seed(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.current_points = 0
        self.turn_total = 0
        
    def roll(self):
        #roll random number between 1 and 6
        self.side = random.choice(Die().sides)
        return(self.side)        

    def hold(self):
        #add points from the turn to current points
        self.current_points += self.turn_total
        self.turn_total = 0
        
        

class Die:
    def __init__(self):
        self.sides = [1,2,3,4,5,6]

        
class Game:
    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        #auto start the game with player1
        self.current_player = self.player1
        self.other_player = self.player2
        
    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player
        
    def reset_game(self):
        self.player1.current_points = 0
        self.player2.current_points = 0
        self.player1.turn_total = 0
        self.player2.turn_total = 0
        self.current_player = self.player1
        self.other_player = self.player2
        
    def start(self):
        #welcome sign
        print(f"Starting game\nThe players are {self.player1.name} and {self.player2.name}")


        #while neither player1 nor player2 has won, keep the game going 
        while self.player1.current_points < 100 and self.player2.current_points < 100:

            #player is asked what they want to do
            decision = input(f"Hello, {self.current_player.name}. Would you like to roll, 'r' or hold, 'h'?: ")
            print()

            #if current player's decision is to roll
            if decision.lower() == "r":

                #call the roll function and set the turn total 
                rolled_num = self.current_player.roll()
                
                
                #if its a 1, current player gets +0 and its now other players turn
                if rolled_num == 1:
                    #add 0 points
                    self.current_player.current_points += 0

                    #reset turn total back to 0
                    self.current_player.turn_total = 0
                    #print message
                    print("-------------------------------")
                    print(f"{self.current_player.name} rolled: {rolled_num}.")
                    print(f"{self.current_player.name}'s gets no additional points and their Current Points are {self.current_player.current_points}")
                    print("-------------------------------\n")

                    
                    self.switch_players()
                          
                #if its a 2-6 the number is added to the player's turn total and the player's turn continues.
                elif rolled_num >= 2 and rolled_num <= 6:

                    #number is added to the player's turn total and the player's turn continues.
                    self.current_player.turn_total += rolled_num
                    print("-------------------------------")
                    print(f"{self.current_player.name} rolled: {rolled_num}.")
                    print(f"{self.current_player.name}'s Turn Total is {self.current_player.turn_total} and Current Points are {self.current_player.current_points}")
                    print("-------------------------------\n")



            #The turn total is added to the player's score and it becomes the opponent's turn.
            elif decision.lower() == "h":
                self.current_player.current_points += self.current_player.turn_total
                print("-------------------------------")
                print(f"{self.current_player.name} chose to hold.")
                print(f"{self.current_player.name}'s Turn Total is {self.current_player.turn_total} and Current Points are {self.current_player.current_points}")
                print("-------------------------------\n")
                self.current_player.turn_total = 0
                self.switch_players()
                
                
            #if player enters an invalid command
            else:
                print("Sorry. Can only accept 'r' or 'h' as commands. Please try again.\n")


        #if the game ends when one of the players gets to 100 points
        if (self.player1.current_points >= 100) or (self.player2.current_points >= 100):

            #picks winnder based on points and output winner message 
            winner = self.player1 if self.player1.current_points >= 100 else self.player2
            print(f"Congratulations {winner.name}! You have won the game with {winner.current_points} points. ")

            #creates ending message and prompt to leave or play again 
            while True:
                ending = input("The game has ended. Would you like to play again? 'y' or 'n': ")
                if ending.lower() == 'n' or ending.lower() == 'y':
                    break
                #if user inputs invalid command
                else:
                    print("Sorry. Can only accept 'y' or 'n' as commands. Please try again.\n")

            #starts game again
            if ending.lower() == 'y':
                self.reset_game()
                self.start()

            #user doesnt want to play anymore
            elif ending.lower() == 'n':
                print("Thank you for playing. Goodbye")

    
    
if __name__ == "__main__":
    
    game = Game()
    game.start()
    
