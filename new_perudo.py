import config
import random
import sys
import time
from bet import Bet
from bet import DUDO
from player import ComputerPlayer
from player import HumanPlayer
from player import CFRPlayer
from strings import correct_dudo
from strings import incorrect_dudo
from strings import INSUFFICIENT_BOTS
from strings import INSUFFICIENT_DICE
from strings import round_title
from strings import welcome_message
from strings import winner

class NewPerudo(self): 
    
    def __init__(self, dice_number_p1, dice_number_p2):
        self.round = 0
        self.nbTotalDices = 0
        self.player = []
        self.players.append(
            CFRPlayer(name="Player 1", dice_number=dice_number_p1, game=self)
        )
        self.players.append(
            CFRPlayer(
                name="Player 2", dice_number=dice_number_p2, game=self
            )
        )
        
        # Roll dice 
        self.roll_dice()
        
        
    # Roll dice for each player
    def roll_dice(self):
        for player in self.players:
            player.roll_dice()
            self.nbTotalDices += len(player.dice)
            
    # Check if a player said dudo!
    def is_dudo(self, quantity, value):
        nbDesBons = 0
        for player in self.players :
            for die in player.dice:
                if (die == value):
                    nbDesBons += 1
        return nbDesBons >= quantity

