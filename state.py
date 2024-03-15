import math
import random

# map avec état -> noeud (qui contient les regrets)
# il faut un tableau de stratégies et un de regrets
# dans un état, il faut l'histoire des actions, les regrets, les stratégies, les valeurs, les noeuds enfants
# il faut :
# - notre information cachée,
#


class State:
    def __init__(self, nbTot, myDice, previousActions, is_palifico_round=False):
        self.nbTotalDices = nbTot
        self.nbDicePlayer = len(myDice)
        self.myDice = myDice
        self.previousActions = previousActions
        self.is_palifico_round = is_palifico_round
        self.nextActions = []

    # Choisir l action dans le tableau d action
    def chooseAction(self):
        if self.nextActions is None:
            self.generateActions()

        # choose action randomly
        return random.choice(self.nextActions)

    # Faire le tableau de toutes les actions possibles
    def generateActions(self):
        # self.previousActions[-1] = [quantité, valeur] (du dernier coup joué, càd du dernier élément du tableau)

        #  Dudo
        self.nextActions.append([1, -1])

        # Si palefico
        if self.is_palifico_round == 1:
            # first player
            if len(self.previousActions) == 0:
                for i in range(1, self.nbTotalDices + 1):
                    for j in range(1, 7):
                        self.nextActions.append([i, j])

            # not the first player
            else:
                for i in range(self.previousActions[-1][0] + 1, self.nbTotalDices + 1):
                    self.nextActions.append([i, self.previousActions[-1][1]])

        # Si c'est un tour normal (pas palefico)
        else:
            # first player
            if len(self.previousActions) == 0:
                for i in range(1, self.nbTotalDices + 1):
                    for j in range(1, 7):
                        self.nextActions.append([i, j])
            else:
                # on augmente la quantité, puis quand on est au max, on augmente la valeur et sa quantité
                if self.previousActions[-1][1] != 1:
                    # générer tout sauf les perudo
                    for i in range(2, self.previousActions[-1][1]):
                        for j in range(
                            self.previousActions[-1][0] + 1, self.nbTotalDices + 1
                        ):
                            self.nextActions.append([j, i])
                    for i in range(self.previousActions[-1][1], 7):
                        for j in range(
                            (
                                self.previousActions[-1][0] + 1
                                if (i == self.previousActions[-1][1])
                                else self.previousActions[-1][0]
                            ),
                            self.nbTotalDices + 1,
                        ):
                            self.nextActions.append([j, i])
                    # générer les perudo
                    for i in range(
                        math.ceil(self.previousActions[-1][0] / 2),
                        self.nbTotalDices + 1,
                    ):
                        self.nextActions.append([i, 1])
                else:  # perudo
                    # générer tous les perudo
                    for i in range(
                        self.previousActions[-1][0] + 1, self.nbTotalDices + 1
                    ):
                        self.nextActions.append([i, 1])
                    # générer les autres (quantité x 2 + 1)
                    for i in range(self.previousActions[-1][1] + 1, 7):
                        for j in range(
                            self.previousActions[-1][0] * 2 + 1, self.nbTotalDices + 1
                        ):
                            self.nextActions.append([j, i])

    # Fonction qui vérifie si l'on est dans un état terminal
    def isTerminal(self):
        return self.previousActions[-1] == [1, -1]

    # Fonction qui retourne la valeur de l'état pour le joueur
    def nextState(self, action):
        new_state = State(
            nbTot=self.nbTotalDices,
            myDice=self.myDice,
            previousActions=self.previousActions + [action],
            is_palifico_round=self.is_palifico_round,
        )
        return new_state

    # Fonction qui crée une stratégie aléatoire
    def generateRandomStrategy(self):
        strategy = {}
        for action in self.nextActions:
            strategy[action] = random.random()
        return strategy
