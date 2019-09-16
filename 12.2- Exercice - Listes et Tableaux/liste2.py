# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]
min = tab[0][0]
indice_x = 0
indice_y = 0
for i in range(len(tab)):
    for j in range(len(tab)):
        if tab[i][j] < min:
            indice_x = i
            indice_y = j
            min = tab[i][j]

print("La valeur maximum est :", min, "et elle se trouve à l'indice [", indice_x," ][ ",indice_y," ]")