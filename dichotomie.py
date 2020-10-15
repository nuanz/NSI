L = [i for i in range(0,101)]
listeVide = []

def dicho(L, val):
  if len(L) == 0:
    return print("error: list is empty")
  
  borne_1 = 0
  borne_2 = len(L)-1
  nbCoups = 0
  end = False

  while end is False:
    nbCoups += 1
    mid = (borne_1+borne_2)//2
    round(mid)

    if L[mid] == val:
      end = True

    elif L[mid] < val:
      borne_1 = mid+1

    else:
      borne_2 = mid-1
  
  return print("{} en indice {}\nTrouvé en {} coups".format(val, mid, nbCoups))
