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



# JOIN 
SELECT regions.nom_region, departements.nom_dept, departements.num_dept
FROM departements JOIN regions
ON departements.num_region = regions.num_region
WHERE regions.nom_region LIKE 'Occitanie' OR regions.nom_region LIKE 'Nouvelle-Aquitaine'
