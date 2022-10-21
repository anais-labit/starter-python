
# importer les modules replace et aléatoire
from dataclasses import replace
import random


# ouvrir file au bon format
file = open("dico_france.txt", encoding = "ISO-8859-1")
# basculer contenu de file dans une variable data
data = file.read()

# créer un tableau des mots contenus
list = data.split()

print(list)

# # remplacer caractères latin
# ac1 = [list.replace ("é", "e") for list in list]
# ac2 = [ac1.replace ("ê", "e") for ac1 in ac1]
# ac3 = [ac2.replace ("è", "e") for ac2 in ac2]
# # print(ac3)
#fermer le fichier
file.close()

def print_word(word, found_letters):
    # print("Mot : ", end="")
    # itère en fonction de la longueur du mot choisi,
    for i in range(len(word)):
        # si le caractère est trouvé, afficher la lettre:        if word[i] in found_letters:        
            if word[i] in found_letters:       
                print(word[i])
            # sinon, afficher "_":
            else:
                print(" _", end="")





def main():
    # choisir un mot aléatoirement 
    word=(random.choice(list))
    print(word)
    lifes = 10
    # stocker les lettres trouvées
    found_letters = set()


    # tant qu'il reste des vies et que le mot n'est pas trouvé :
    while lifes > 0:
        # convoquer fonction qui traite l'affichage du mot
        print_word(word, found_letters)
        
        #indiquer le nombre de vies
        print("Tu as ", lifes, " vies ")

        # demander lettre à essayer
        letter=input("\nQuelle lettre veux-tu essayer ? ").lower
        
        # si la lettre n'est pas dans le mot, décrémenter d'une vie
        if letter not in word:
            lifes =-1

        # si plus de vies = perdu
        if lifes == 0:
            print("Perdu ! Le mot était ", word)

        
        break

main()