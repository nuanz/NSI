class nim:
  def __init__(self, j1, j2, alu):
    self.j1 = "Arno"
    self.j2 = "Egxon"
    self.alu= alu

  def texte (self,j1,j2):
    print("Les joueurs sont", self.j1, "et", self.j2)
    print("On a", self.allumettes, "sur la table, jouez !")

  def Afficher(self):
    return print(jeu1.alu)

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
tour = int(input('Ecrivez 0 pour que le joueur 1 commence et 1 pour que ce soit le joueur 2 :'))

jeu1=nim(j1,j2,alu)
jeu1.Afficher()

while jeu1.alu > 1 :
  
  if tour % 2 == 0:
    nombre = int(input(j1+" combien d'allumettes veux-tu retirer ?"))
    if jeu1.verifie(nombre) is True:
      jeu1.alu = jeu1.alu - nombre
      tour=tour+1
      jeu1.Afficher()

    else:
      print("Rejouez:")

  else :
    nombre = int(input(j2+" combien d'allumettes veux-tu retirer ?"))
    if jeu1.verifie(nombre) is True:
      jeu1.alu = jeu1.alu - nombre
      tour=tour+1
      jeu1.Afficher()

    else:
      print("Rejouez:")



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
