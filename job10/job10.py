question=input("Comment est votre blanquette ? ")

#a, pour une ouverture en mode ajout à la fin du fichier (APPEND). 
# Si le fichier n'existe pas python le crée.
file = open("output.txt", "a")
#écriture
file.write(question)

#r, pour une ouverture en lecture (READ)
file = open("output.txt", "r")
reponse = file.read()
#affichage du contenu
print(reponse)

#fermer le fichier
file.close()