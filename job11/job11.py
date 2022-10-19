
# céer une liste dans laquelle stocker les données que l'on va chercher :
list = []

# définir la valeur de la variable à chercher dans le fichier file :
word = '"domain">'

# ouvrir et lire file :
file = open("domains.xml", "r")

# basculer les lignes de file dans la variable content :
content = file.readlines()

# s'il n'y a pas word = "-1", sinon = "25", soit index de word
# pour chaque ligne de content, si word != -1, l'ajouter à la liste :
for line in content:
    if line.find(word) != -1:
        list.append(line)

# afficher le nombre d'entrées enregistrées dans la liste :
print(len(list))

#fermer le fichier
file.close()