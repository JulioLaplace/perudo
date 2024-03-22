import random
import math

from state import State
from new_perudo import NewPerudo



# code qui ne marche pas mais qui est la pour donner une idée de ce qu'il faut faire
class CFR:
    def __init__(self, nbIterations):
        self.node_map = {}
        self.history = []
        self.nbIterations = nbIterations

    # Entraîner l'algorithme
    def train(self):
        # Créer un jeu de Perudo avec 2 HumanPlayer ayant comme id 0 et 1
        for _ in range(self.nbIterations):
            game = self.gameReset()
            # Créer une configuration de jeu aléatoire
            self.cfr(game, 0, 1, 1)

    # Fonction principale de l'algorithme cfr
    def cfr(self, game, player, pi, po):
        print("cfr")
        # Si l'état du jeu est terminal, retourner la valeur de l'état pour le joueur
        if self.isTerminal():
            print("isTerminal")
            if game.isDudo(self.history[-1][0], self.history[-1][1]):
                return -1
            else:
                return 1
        # begin cfr 
        actions = self.generateActions(game)
        number_of_actions = len(actions)
        node = None
        currentKey = [self.history, game.nbTotalDices, game.players[player].dice]
        if self.isKeyInNodeMap(tuple(tuple(tuple(x) if isinstance(x, list) else x for x in currentKey[0]) if isinstance(x, list) else x for x in currentKey)): # peut etre va falloir changer ça(comparer élément par élement)
            node = self.node_map[tuple(tuple(tuple(x) if isinstance(x, list) else x for x in currentKey[0]) if isinstance(x, list) else x for x in currentKey)]
        else:
            node = self.generateNode(actions)
            self.node_map[tuple(tuple(tuple(x) if isinstance(x, list) else x for x in currentKey[0]) if isinstance(x, list) else x for x in currentKey)] = node

        # Créer une stratégie depuis les regrets
        strategy = self.getStrategyFromRegrets(node)
        
        # utils 
        utils = [0.0] * number_of_actions
        node_util = 0.0            
        
        
        # on balaye les actions possibles
        for a in range(number_of_actions):
            self.next(actions[a])
            if player == 0:
                utils[a] = - self.cfr(game, 1, pi * strategy[a], po)
            else:
                utils[a] = - self.cfr(game, 0, pi, po * strategy[a])
            self.undo()
            node_util += strategy[a] * utils[a]
            
        for a in range(number_of_actions):
            regret = utils[a] - node_util
            # node[1] = regrets_sum
            node[1][a] += (po if player == 0 else pi) * regret
        self.updateStrategySum(node, strategy, pi if player == 0 else po)
        return node_util
            
        
    def updateStrategySum(self, node, strategy, p):
        # node[0] = strategy_sum
        for i in range(len(node[0])):
            node[0][i] += p * strategy[i]
    
    def next(self, action):
        self.history.append(action)
        
    def undo(self):
        self.history.pop()

    def gameReset(self):
        print("gameReset")
        return NewPerudo(random.randint(1, 2), random.randint(1, 2)) 
    
    def isTerminal(self):
        if len(self.history) == 0:
            return False
        # get last element of history 
        return self.history[-1] == [1, -1]
    
    # Faire le tableau de toutes les actions possibles
    def generateActions(self, game):
        # self.previousActions[-1] = [quantité, valeur] (du dernier coup joué, càd du dernier élément du tableau)

        nextActions = []
        #  Dudo
        nextActions.append([1, -1])

        # # Si palefico
        # if self.is_palifico_round == 1:
        #     # first player
        #     if len(self.previousActions) == 0:
        #         for i in range(1, self.nbTotalDices + 1):
        #             for j in range(1, 7):
        #                 self.nextActions.append([i, j])

        #     # not the first player
        #     else:
        #         for i in range(self.previousActions[-1][0] + 1, self.nbTotalDices + 1):
        #             self.nextActions.append([i, self.previousActions[-1][1]])

        # Si c'est un tour normal (pas palefico)
        # else:
            # first player
        if len(self.history) == 0:
            for i in range(1, game.nbTotalDices + 1):
                for j in range(1, 7):
                    nextActions.append([i, j])
        else:
            # on augmente la quantité, puis quand on est au max, on augmente la valeur et sa quantité
            if self.history[-1][1] != 1:
                # générer tout sauf les perudo
                for i in range(2, self.history[-1][1]):
                    for j in range(
                        self.history[-1][0] + 1, game.nbTotalDices + 1
                    ):
                        nextActions.append([j, i])
                for i in range(self.history[-1][1], 7):
                    for j in range(
                        (
                            self.history[-1][0] + 1
                            if (i == self.history[-1][1])
                            else self.history[-1][0]
                        ),
                        game.nbTotalDices + 1,
                    ):
                        nextActions.append([j, i])
                # générer les perudo
                for i in range(
                    math.ceil(self.history[-1][0] / 2),
                    game.nbTotalDices + 1,
                ):
                    nextActions.append([i, 1])
            else:  # perudo
                # générer tous les perudo
                for i in range(
                    self.history[-1][0] + 1, game.nbTotalDices + 1
                ):
                    nextActions.append([i, 1])
                # générer les autres (quantité x 2 + 1)
                for i in range(self.history[-1][1] + 1, 7):
                    for j in range(
                        self.history[-1][0] * 2 + 1, game.nbTotalDices + 1
                    ):
                        nextActions.append([j, i])
        return nextActions
    
    def generateNode(self, actions):
        strategy_sum = []
        regrets_sum = []
        actions = actions
        for i in range(len(actions)):
            strategy_sum.append(0)
            regrets_sum.append(0)
            
        return [strategy_sum, regrets_sum, actions]
    
    def isKeyInNodeMap(self, tupleCurrentKey):
        return tupleCurrentKey in self.node_map
            
    def getStrategy(self, array):
        n = len(array)
        strategy = [0.0] * n
        s = sum(max(0.0, v) for v in array)
        for i in range(n):
            strategy[i] = max(0.0, array[i]) / s if s != 0.0 else 1.0 / float(n)
        return strategy

    def getStrategyFromRegrets(self, node):
        return self.getStrategy(node[1])