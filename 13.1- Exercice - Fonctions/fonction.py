# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(tab_lettres)


def afficherfrequence():
    for i in range(len(tab_lettres[0])):
        for j in range(len(texte)):
            if tab_lettres[0][i] == texte[j]:
                tab_lettres[1][i] += 1


afficherfrequence()

print(tab_lettres)

for i in range(len(tab_lettres[0])):
    if tab_lettres[0][i] == " ":
        print("L'espace est présent ", tab_lettres[1][i], "fois.")
    else:
        print("La lettre", tab_lettres[0][i], "apparaît", tab_lettres[1][i], "fois.")