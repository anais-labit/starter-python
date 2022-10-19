from random import randint

price = randint(70, 200)

nb_essais = 1
nb_essais_max = 5

guess = int(input("""Devinez le prix de cette machine à café ! Vous avez 5 essais ! C'est parti !
Saisissez un nombre entre 70 et 200 : """))

#tant que sa réponse est différente du prix et que nb_essais est inférieur à nb_essais_max
while guess != price and nb_essais < nb_essais_max:

        #et si sa réponse est supérieure au prix, on le lui indique, redemande, et ajoute 1 à nb_essais
        if guess > price:
            guess = int(input("Non ! C'est moins... Essayez encore : "))
            nb_essais += 1

        #sinon (c'est à dire réponse inférieure), on le lui indique, redemande, et ajoute 1 à nb_essais
        elif guess < price:
            guess = int(input("Non ! C'est plus... Essayez encore : "))
            nb_essais += 1

#mais si sa réponse est égale au prix et que nb_essais est inférieur ou égal à nb_essais_max, afficher bravo
if guess == price and nb_essais <= nb_essais_max:
    print("Bravo ! Cette machine à café d'une valeur de {}€ est à vous !".format(guess))

#sinon (c'est à dire nb_essais_max dépassé), afficher perdu
else:
    print("Dommage, c'est perdu ! Le juste prix était {}€".format(price))

