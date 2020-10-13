class nim:
  def __init__(self, alu, tour, gagnant = "",):
    self.j1 = j1
    self.j2 = j2
    self.alu=alu
    self.tour= tour
    self.gagnant=""

  def texte (self,j1,j2):
    print("Les joueurs sont", self.j1, "et", self.j2)
    print("On a", self.allumettes, "sur la table, jouez !")

  def Afficher(self):
    print(jeu1.alu)

  def verifie(self, nombre):
    if 1 <= nombre <= 3 :
      return True
    else :
      print("Vous ne pouvez pas enlever {}".format(nombre))
      return False
      

  def gagnant(self):
     if self.alu <=1:
       print(" Fin de jeu")
       return True
     else:
       return False

j1= input("Choisi ton nom j1 :")
j2= input("Choisi ton nom j2 :")
alu =int(input("Nombre d'allumettes ?"))

jeu1=nim(alu,j1,j2)
jeu1.Afficher()
tour = int(input('Ecrivez 0 pour que le joueur 1 commence et 1 pour que ce soit le joueur 2 :'))

while jeu1.alu > 1 :
  
  if tour % 2 == 0:
    joueur1 = j1
    nombre = int(input(j1+" combien d'allumettes veux-tu retirer ?"))
    if jeu1.verifie(nombre) is True:
      jeu1.alu = jeu1.alu - nombre
      tour=tour+1
      print(jeu1.alu)
    else:
      tour = tour - 1

  else :
    joueur2 = j2
    nombre = int(input(j2+" combien d'allumettes veux-tu retirer ?"))
    if jeu1.verifie(nombre) is True:
      jeu1.alu = jeu1.alu - nombre
      tour=tour+1
      print(jeu1.alu)
    else:
      tour = tour - 1

if jeu1.alu == 1:
  if tour%2 == 0:
    print ("Bravo  {} !! Tu as gagné".format(j2))
  else:
    print ("Bravo  {} !! Tu as gagné".format(j1))
else:
  if tour%2 == 0:
    print ("Bravo  {} !! Tu as gagné".format(j1))
  else:
    print ("Bravo  {} !! Tu as gagné".format(j2))
  
