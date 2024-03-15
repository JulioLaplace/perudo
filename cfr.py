# # Fonction CFR(état_du_jeu, joueur):
# #     Si l'état_du_jeu est un état terminal:
# #         retourner la valeur de l'état pour le joueur

# #     Si joueur est un joueur chanceux:
# #         choisir une action selon la distribution de probabilité déterministe
# #         retourner CFR(état_du_jeu.résultant_de(l'action), joueur)

# #     Si joueur est un joueur adverse:
# #         Pour chaque action possible a du joueur dans l'état_du_jeu:
# #             Pour chaque information cachée h du joueur dans l'état_du_jeu:
# #                 calculer la probabilité stratégique de jouer a en fonction de regrets cumulés
# #             Choisir une action selon la distribution de probabilité stratégique
# #             Calculer la probabilité d'action choisie
# #             Pour chaque information cachée h du joueur dans l'état_du_jeu:
# #                 CFR(état_du_jeu.résultant_de(l'action), joueur)
# #                 Mettre à jour les regrets en fonction de la valeur du jeu

# # Fonction mettre_à_jour_les_regrets(état_du_jeu, joueur, poids):
# #     Si l'état_du_jeu est un état terminal:
# #         retourner la valeur de l'état pour le joueur * poids

# #     Pour chaque action a du joueur dans l'état_du_jeu:
# #         regret = valeur_de_l'état - CFR(état_du_jeu, joueur)
# #         Ajouter regret * poids à regrets[a]

# # Fonction mise_à_jour_stratégie(état_du_jeu, joueur):
# #     Pour chaque information cachée h du joueur dans l'état_du_jeu:
# #         Pour chaque action a du joueur dans l'état_du_jeu:
# #             Calculer la probabilité stratégique de jouer a en fonction de regrets cumulés
# #             Enregistrer la probabilité stratégique mise à jour


# import random
# from state import State
# from perudo import Perudo


# # code qui ne marche pas mais qui est la pour donner une idée de ce qu'il faut faire
# class CFR:
#     def __init__(self, nbIterations):
#         self.regrets = {}
#         self.strategy = {}
#         self.state = None
#         self.nbIterations = nbIterations

#     # Entraîner l'algorithme
#     def train(self):
#         # Créer un jeu de Perudo avec 2 HumanPlayer ayant comme id 0 et 1
#         game = Perudo("Moi", 1, 5)
#         for _ in range(self.nbIterations):
#             # Créer une configuration de jeu aléatoire
#             self.cfr(game, 0, 1, 1)

#     # Fonction principale de l'algorithme cfr
#     def cfr(self, game, player, pi, po):


#     # Fonction qui exécute une itération
#     def runIteration(self):
#         # Mettre à jour les regrets et les stratégies pour l'état initial
#         self.updateStrategy(self.state)
#         self.updateRegrets(self.state)

#         # Propagation des actions jusqu'à un état terminal
#         while not self.state.isTerminal():
#             action = self.state.chooseAction()
#             self.state = self.state.nextState(action)

#             # Mettre à jour les regrets et les stratégies pour l'état suivant
#             self.updateStrategy(self.state)
#             self.updateRegrets(self.state)

#     # Mettre à jour les regrets
#     def updateRegret(self, state):
#         if state not in self.regrets:
#             self.regrets[state] = {}

#         # Pour chaque action possible dans l'état
#         for action in state.nextActions:
#             # Calculer la récompense réelle pour l'action
#             new_state = state.nextState(action)
#             reward = self.computeReward(new_state)  # À implémenter

#             # Calculer la récompense attendue pour l'action en utilisant les stratégies actuelles
#             expected_reward = self.computeExpectedReward(state, action)  # À implémenter

#             # Calculer le regret associé à l'action
#             regret = expected_reward - reward

#             # Accumuler le regret dans le dictionnaire regrets
#             if action not in self.regrets[state]:
#                 self.regrets[state][action] = 0
#             self.regrets[state][action] += regret

#         # Méthode pour calculer la récompense réelle pour un état donné

#     def computeReward(self, state):
#         if state.isTerminal():


#     # Méthode pour calculer la récompense attendue pour une action donnée dans un état donné
#     def computeExpectedReward(self, state, action):
#         expected_reward = 0
#         for a in state.nextActions:
#             if a not in self.strategies.get(state, {}):
#                 continue
#             prob = self.strategies[state][a]
#             new_state = state.nextState(a)
#             reward = self.computeReward(new_state)
#             expected_reward += prob * reward
#         return expected_reward

#     # Mettre à jour les stratégies
#     def updateStrategy(self, state):
#         pass
