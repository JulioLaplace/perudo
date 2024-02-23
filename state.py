import math

class State:
    def __init__(self,nbTot, myDice, nbDicePlayer,lastQ,lastV):
        self.nbTotalDices = nbTot
        self.nbDicePlayer =nbDicePlayer
        self.myDice=myDice
        self.lastQty=lastQ
        self.lastVal=lastV
        self.actions=[]
        
    # Choisir l action dans le tableau d action
    def chooseAction(self):  
        
        
    # Faire le tableau de toutes les actions possibles
    def generateActions(self):

        #  Dudo
        self.actions.append([-1, 1])
        # first player
        if self.lastQty==0:

        #  On est pas le premier a jouer 
        else:
            #  Si le dernier bet nest pas sur un perudo
            if self.lastVal != 1 : 
                for i in range(self.lastQ+1, self.nbDicePlayer+1):
                    self.actions.append([i,self.lastVal])
                for i in range(self.lastVal+1, 7):
                    self.actions.append([self.lastQty,i])
                # Perudo
                for i in range(math.ceil(self.lastQty/2), self.nbDicePlayer+1):
                    self.actions.append([i,1]) 
            
            # Si le dernier bet est sur un perudo
            else : 

                

            
