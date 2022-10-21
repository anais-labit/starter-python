# Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
# jeu le pendu dans le terminal.
# Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
# souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
# débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
# niveau.
# Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
# ici, et afficher :
# - Le nombre de vies restantes au joueur
# - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
# En expert, la liste n’apparaîtra pas)
# - Des “_” pour remplacer les lettres non trouvées
# - Les lettres proposées qui se trouvent dans le mot
# La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.


# importer les modules replace et aléatoire
from dataclasses import replace
import random

# ouvrir file au bon format
file = open("dico_france.txt", encoding = "ISO-8859-1")
# basculer contenu de file dans une variable data
data = file.readlines()
# remplacer caractères latin
ac1 = [data.replace ("é", "e") for data in data]
ac2 = [ac1.replace ("ê", "e") for ac1 in ac1]
ac3 = [ac2.replace ("è", "e") for ac2 in ac2]
# print(ac3)
#fermer le fichier
file.close()

# choisir un mot aléatoirement 
word=(random.choice(ac3))

# compter le nombre de caractère du mot
char_nb=((len(word))-1)

# remplacer char_nb par autant de "_" que le mot compte de caractères
user_guess=(char_nb*" _ ")

list_user_guess=list(user_guess)
list_word=list(word)

# bienvenue et demander niveau
print()
level=input("Bienvenue ! Quel niveau choisis-tu (1, 2 ou 3) ? ")
print()
if level == "1":
    lifes = 10

if level == "2":
    lifes = 7

if level == "3":
    lifes = 4

# print lifes + char
print("Tu as le droit à", lifes, "mauvaises réponses pour trouver le mot suivant :\n", user_guess)

# tant qu'il reste des vies et que le mot n'est pas complet :
while lifes != 0 or user_guess != word:
    # demander lettre à essayer
    print()
    letter=(input("Quelle lettre veux-tu essayer ? ")).lower()

    # si la lettre est dans le mot, 
    if letter in list_word:
        
        # que index+1 est inféreur ou égal au nombre de caractères du mot, 
        # i=0
        for i in range(char_nb):
            # si ma lettre correspond à un index du mot, je remplace le même index de list_user_guess par la lettre : 
            if letter == word[i]:
                list_user_guess[i]=letter
                i=+1
        print(list_user_guess)

    # sinon ajouter letter à tried_letters
    else:
        # enlever 1 à lifes
        lifes -=1
        print()
        print("Il te reste ", lifes, " ratés possibles ! ")
        # créer une liste et y ajouter les lettres déjà essayées
        tried_letters=[]
        if letter is not tried_letters:
            tried_letters.append(letter)
            print()
            print("Voici les lettres déjà essayées : ", tried_letters)
    
        # # elif lifes == 0 or guess == word :
        #     # break

        #     else:
        #     print "raté" + lifes + liste tried_letters
        #     restart()

main()





        # ..................




