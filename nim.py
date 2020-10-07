import random # Importation de la bibliothèque 'random'
class Nim:
    #INSTANCIATION
    def __init__ (self, nbAllumettes=12, nomA="Joueur1", nomB="Joueur2"):
        self.j1 = nomA
        self.j2 = nomB
        self.allumettes = nbAllumettes
        self.tour = 0
   
    #METHODE DE JEU
    def enlever(self, nb):
        self.allumettes -= nb
        return self.allumettes
   
    #VERIF
    def verifie(self, nb):
        if 1 <= nb <= 3: # Si le nombre est compris entre 1 et 3
            return True # Alors c'est bon
        else: # Sinon message d'erreur
            print("\nVous ne pouvez pas enlever {} allumettes. Il reste {} allumettes\n".format(nb, self.allumettes))
            return False # Et on retourne Faux
   
    #FIN DE JEU
    def termine(self):
        if self.allumettes <= 1: #Si l'on tomnbe à 1 allumette ou moins
            return True # La partie est terminée
        else: # Sinon
            return False # La partie continue
   
    def bravo(self, gagnant):
        return print("\n\nBravo {} !\n\n".format(gagnant))

#MENU
j1 = str(input("Entrez le nom du joueur 1 :\n"))
j2 = str(input("Entrez le nom du joueur 2 :\n"))
a = int(input("Avec combien d'allumettes voulez-vous jouer ?\n"))

#INITIALISATION DE LA PARTIE
Game = Nim(a, j1, j2)
joueurs = []

#GENERATION DE LA LISTE ALEATOIRE DES JOUEURS
if random.random() > 0.5:
    joueurs.append(j1), joueurs.append(j2)
else:
    joueurs.append(j2), joueurs.append(j1)

#JEU
while Game.termine() is False: # Tant qu'il ne reste pas une allumette ou moins

  # QUI DOIT JOUER ?
  Game.tour += 1 # +1 tour
  joueur = joueurs[(Game.tour%2)] # On travaille l'indice pour connaître le joueur qui joue en sachant si le nombre de tour est pair ou non (0 et 1 donc indice 0 et 1)

  # DEBUT DU TOUR
  nombre = int(input("\nIl reste {} allumettes\nC'est au tour de {} de jouer. Combien d'allumettes enlevez-vous ?\n".format(Game.allumettes, joueur)))
 
  # VERIF ARRIERE PLAN
  if Game.verifie(nombre) is True : # Si le nombre respecte les règles
    Game.enlever(nombre) # On enlève les allumettes
  else: # Sinon
    Game.tour -= 1 # On revient dans la boucle avec un tour de moins (reset de tour, le joueur rejoue)
 
  # TEST DE FIN DE JEU
  Game.termine()

#MESSAGE DE FIN DE JEU    
if Game.allumettes == 1: # S'il reste une seule allumette
  Game.bravo(joueur) # Le joueur qui vient de jouer a gagné car l'autre n'a plus d'options et doit enlever la dernière allumette
else: # Sinon, si il enlève la dernière, il perd
  Game.bravo(joueurs[((Game.tour+1)%2)]) # C'est alors l'autre joueur qui gagne (On rajoute 1 au tour pour changer l'indice; cf com. ligne 51.
