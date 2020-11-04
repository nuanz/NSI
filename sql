#SOMME DE TOUS LES ATTRIBUTS

SELECT SUM(attribut)
FROM table



#COMPTE LE NOMBRE DE VALEURS DANS L'ATTRIBUT 

SELECT COUNT(attribut)
FROM table



#LIMITER LE NOMBRE DE RESULTATS

SELECT attribut
FROM table ORDER BY attribut LIMIT max



# 

SELECT attribut, COUNT(*) AS nouvelle_colonne 
FROM table GROUP BY attribut
ORDER BY nouvelle_colonne 



#

SELECT attribut1, SUM(attribut2) AS nouvelle_colonne 
FROM table GROUP BY attribut1
ORDER BY nouvelle_colonne



# Longueur

LENGTH(attribut)

pute
