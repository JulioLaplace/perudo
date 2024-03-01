# Fonction CFR(état_du_jeu, joueur):
#     Si l'état_du_jeu est un état terminal:
#         retourner la valeur de l'état pour le joueur

#     Si joueur est un joueur chanceux:
#         choisir une action selon la distribution de probabilité déterministe
#         retourner CFR(état_du_jeu.résultant_de(l'action), joueur)

#     Si joueur est un joueur adverse:
#         Pour chaque action possible a du joueur dans l'état_du_jeu:
#             Pour chaque information cachée h du joueur dans l'état_du_jeu:
#                 calculer la probabilité stratégique de jouer a en fonction de regrets cumulés
#             Choisir une action selon la distribution de probabilité stratégique
#             Calculer la probabilité d'action choisie
#             Pour chaque information cachée h du joueur dans l'état_du_jeu:
#                 CFR(état_du_jeu.résultant_de(l'action), joueur)
#                 Mettre à jour les regrets en fonction de la valeur du jeu

# Fonction mettre_à_jour_les_regrets(état_du_jeu, joueur, poids):
#     Si l'état_du_jeu est un état terminal:
#         retourner la valeur de l'état pour le joueur * poids

#     Pour chaque action a du joueur dans l'état_du_jeu:
#         regret = valeur_de_l'état - CFR(état_du_jeu, joueur)
#         Ajouter regret * poids à regrets[a]

# Fonction mise_à_jour_stratégie(état_du_jeu, joueur):
#     Pour chaque information cachée h du joueur dans l'état_du_jeu:
#         Pour chaque action a du joueur dans l'état_du_jeu:
#             Calculer la probabilité stratégique de jouer a en fonction de regrets cumulés
#             Enregistrer la probabilité stratégique mise à jour


import random
from state import State


class CFR:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.regrets = {}
        self.strategy = {}
        self.average_strategy = {}
        self.iterations = 1000

    def cfr(self, state, weight):
        if state.isTerminal():
            return state.value(self.player) * weight

        if state.isPlayerChance():
            action = state.chooseAction()
            new_state = state.resultingState(action)
            return self.cfr(new_state, weight)

        player = state.player()
        if player == self.player:
            return self.cfrForPlayer(state, weight)
        else:
            return self.cfrForOpponent(state, weight)

    def cfrForPlayer(self, state, weight):
        action_utilities = {}
        strategy = (
            self.strategy[state]
            if state in self.strategy
            else state.generateRandomStrategy()
        )
        for action in state.actions:
            action_utilities[action] = self.cfr(
                state.resultingState(action), weight * strategy[action]
            )
        for action in state.actions:
            self.regrets[state][action] += action_utilities[action]
        return sum(action_utilities.values())

    def cfrForOpponent(self, state, weight):
        action_utilities = {}
        strategy = (
            self.strategy[state]
            if state in self.strategy
            else state.generateRandomStrategy()
        )
        for action in state.actions:
            action_utilities[action] = self.cfr(state.resultingState(action), weight)
        for action in state.actions:
            self.regrets[state][action] += action_utilities[action]
        return sum(action_utilities.values())

    def updateStrategy(self, state):
        strategy_sum = 0
        for action in state.actions:
            strategy_sum += max(0, self.regrets[state][action])
        for action in state.actions:
            self.strategy[state][action] = (
                max(0, self.regrets[state][action]) / strategy_sum
            )
            self.average_strategy[state][action] += self.strategy[state][action]

    def train(self):
        for i in range(self.iterations):
            self.cfr(self.game.initialState(), 1)
            for state in self.strategy:
                self.updateStrategy(state)
        for state in self.average_strategy:
            strategy_sum = 0
            for action in state.actions:
                strategy_sum += self.average_strategy[state][action]
            for action in state.actions:
                self.average_strategy[state][action] /= strategy_sum
        return self.average_strategy
