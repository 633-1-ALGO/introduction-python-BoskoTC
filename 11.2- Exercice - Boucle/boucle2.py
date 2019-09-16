# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]
min = 0
for i in range(0, len(B)):
    min = B[i]
    j = i - 1
    while j >= 0 and B[j] > min:
        B[j + 1] = B[j]
        j = j - 1
    B[j + 1] = min

for i in range(len(B)):
    print(B[i])