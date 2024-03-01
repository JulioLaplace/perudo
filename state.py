import math
import random


class State:
    def __init__(self, nbTot, myDice, nbDicePlayer, lastQ, lastV):
        self.nbTotalDices = nbTot
        self.nbDicePlayer = nbDicePlayer
        self.myDice = myDice
        self.lastQty = lastQ
        self.lastVal = lastV
        self.actions = []

    # Choisir l action dans le tableau d action
    def chooseAction(self):
        if self.actions is None:
            self.generateActions()

        # choose action randomly
        return random.choice(self.actions)

    # Faire le tableau de toutes les actions possibles
    def generateActions(self):

        #  Dudo
        self.actions.append([1, -1])

        # first player
        if self.lastQty == 0:
            for i in range(1, self.nbTotalDices + 1):
                for j in range(1, 7):
                    self.actions.append([i, j])
        else:
            # on augmente la quantité, puis quand on est au max, on augmente la valeur et sa quantité
            if self.lastVal != 1:
                # générer tout sauf les perudo
                for i in range(self.lastVal, 7):
                    for j in range(
                        self.lastQty + 1 if (i == self.lastVal) else self.lastQty,
                        self.nbTotalDices + 1,
                    ):
                        self.actions.append([j, i])
                # générer les perudo
                for i in range(math.ceil(self.lastQty / 2), self.nbTotalDices + 1):
                    self.actions.append([i, 1])
            else:  # perudo
                # générer tous les perudo
                for i in range(self.lastQty + 1, self.nbTotalDices + 1):
                    self.actions.append([i, 1])
                # générer les autres (quantité x 2 + 1)
                for i in range(self.lastVal + 1, 7):
                    for j in range(self.lastQty * 2 + 1, self.nbTotalDices + 1):
                        self.actions.append([j, i])

    # Fonction qui vérifie si l'on est dans un état terminal
    def isTerminal(self):
        return self.nbTotalDices == 0

    # Fonction qui retourne la valeur de l'état pour le joueur
    def resultingState(self, action):
        new_state = State(self.nbTotalDices - action)
        new_state.player = 1
        return new_state

    # Fonction qui crée une stratégie aléatoire
    def generateRandomStrategy(self):
        strategy = {}
        for action in self.actions:
            strategy[action] = random.random()
        return strategy
