# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

nb_occurence = texte.count("exemple")

print("Le mot 'exemple' apparaît", nb_occurence, "fois.\n")

texte = texte.replace("est", "représente")
print(texte)

print(texte[::-1])
