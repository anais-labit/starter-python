def fun(*numbers):

    #créer une liste vide
    myList=[]

    # pour chaque nombre saisi en paramètre, l'enregistrer dans la liste
    for number in numbers:
        myList.append(number)

    # trier ma liste (ordre croissant par défaut)
    myList.sort()
    print("Mes chiffres par odre croissant :"  + str(myList))

fun(1, 3, 4, 7, 9, 7, 56, 32)
