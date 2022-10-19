# ouvrir file
file = open("data.txt", "r")

# basculer contenu de file dans une variable content
content = file.read()

#convertir content en tableau et enregister son nombre d'entrées dans une nouvelle variable
filtered_content = len(content.split())

# afficher la variable
print(filtered_content)

#fermer le fichier
file.close()