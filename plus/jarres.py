from random import *
keys = 2

print("""Bienvenue ! Vous avez face à vous 5 jarres : 4 contiennent 1 clé magique, la 5ème contient 1 serpent !
Il vous faudra 6 clés pour gagner la partie. Dès que votre trousseau tombe à 0, vous perdez ! 
Vous avez 2 clés offertes pour commencer, bonne chance !""")

while keys != 0 and keys != 6:

    snake = randint(1, 5)
    print(snake)
    guess = int(input("Dans quelle jare est le serpent (1,2,3,4 ou 5) ? "))

    if guess == snake:
        keys -= 1
        print("Jarre piègée ! Vous perdez ! Vous avez",keys,"clé(s)")
                                
    else:
        keys += 1
        print("Jarre trésor ! Vous gagnez ! Vous avez",keys,"clé(s)")

if keys == 6:
    print("Félicitations ! Vous devenez Roi du temple !")

if keys == 0:
    new_game = input("Vous avez perdu... Voulez-vous jouer une autre partie (yes or no) ?")
    if new_game == "yes":

        keys = 2

        print("""Bienvenue ! Vous avez face à vous 5 jarres : 4 contiennent 1 clé magique, la 5ème contient 1 serpent !
Il vous faudra 6 clés pour gagner la partie. Dès que votre trousseau tombe à 0, vous perdez ! 
Vous avez 2 clés offertes pour commencer, bonne chance !""")

        while keys != 0 and keys != 6:
            snake = randint(1, 5)
            guess = int(input("Dans quelle jare est le serpent (1,2,3,4 ou 5) ? "))

            if guess == snake:
                keys -= 1
                print("Jarre piègée ! Vous perdez ! Vous avez",keys,"clé(s)")
                                        
            else:
                keys += 1
                print("Jarre trésor ! Vous gagnez ! Vous avez",keys,"clé(s)")

        if keys == 6:
            print("Félicitations ! Vous devenez Roi du temple !")

        if keys == 0:
            new_game = input("Vous avez perdu... Voulez-vous jouer une autre partie (yes or no) ?")
            






