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
# fermer le fichier
file.close()

# choisir un mot aléatoirement 
word=(random.choice(ac3))

# compter le nombre de caractère du mot
char_nb=((len(word))-1)

# remplacer char_nb par autant de "_" que le mot compte de caractères
user_guess=(char_nb*"_")

list_user_guess=list(user_guess)
list_word=list(word)
list_word.remove('\n')
tried_letters=[]
#print(word)

# bienvenue et demander niveau
level=input("\nBienvenue ! Quel niveau choisis-tu (1, 2 ou 3) ? \n")
if level == "1":
    lifes = 10

if level == "2":
    lifes = 7

if level == "3":
    lifes = 4

def replace(letter):
    # tant que index+1 est inféreur ou égal au nombre de caractères du mot, 
    for i in range(char_nb):
        # si ma lettre correspond à un index du mot, je remplace le même index de list_user_guess par la lettre : 
        if letter == word[i]:
            list_user_guess[i]=letter
            i=+1
    print(" ".join(list_user_guess))

def main(lifes):
    # print lifes + char
    print("\nTu as le droit à", lifes, "mauvaises réponses pour trouver le mot suivant :\n", user_guess)

    # tant qu'il reste des vies et que le mot n'est pas complet :
    while lifes != 0 or user_guess != word:
        # demander lettre à essayer
        letter=(input("\nQuelle lettre veux-tu essayer ? \n")).lower()
        print()
        # si la lettre est dans le mot, 
        if letter in list_word:
            replace(letter)

        # sinon ajouter letter à tried_letters
        else:
            # enlever 1 à lifes
            lifes -=1
            print("\nIl te reste ", lifes, " mauvaises réponses possibles !\n")
          # envoyer lettre dans tried_letters
            if letter is not tried_letters:
                tried_letters.append(letter)
                print("\nVoici les lettres déjà essayées : ", tried_letters,"\n")
    
        if list_user_guess == list_word:
            return print("Gagné !")
            
        if lifes == 0:
            return print("Perdu ! Le mot était : ", word)

main(lifes)