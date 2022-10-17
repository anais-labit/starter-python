

# analyser les entiers de 1 à 100
for i in range(1, 100):

    # si le reste de la division par 3 = 0 et par 5 = 0 
    if i%3 == 0 and i%5 == 0:
        # afficher :
        print("FizzBuzz")

    # si le reste de la division par 3 = 0
    elif i%3 == 0:
        # afficher :
        print("Fizz")

    # si le reste de la division par 5 = 0
    elif i%5 == 0:
        # afficher :
        print("Buzz")
    

    # sinon afficher l'entier
    else:
        print(i)
