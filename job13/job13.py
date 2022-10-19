# saisir le nb de lettres des mots à chercher
letters_nb = int(input("Saisir un nombre entier : "))

# ouvrir, lire et basculer le contenu de file dans content
file = open("data.txt", "r")
content = file.read()

# définir le début du compteur
nb_words = 0

# pour chaque ligne de content, spliter les lignes et les enregistrer dans list
list = content.split()

# pour chaque mot de list, si la longueur est égale au nb de lettres voulu,
# incrémenter de 1 nb_words à chaque tour de boucle 
for word in list:
    if len(word) == letters_nb:
        nb_words = nb_words +1

# afficher le nombre de mots qui possèdent le bon nb de lettres

print("Le nombre de mots à " + str(letters_nb) + " lettres est : " + str(nb_words))

#fermer le fichier
file.close()

