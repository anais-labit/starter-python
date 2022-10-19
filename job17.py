def fun(*numbers):
    # print(numbers)
    
    # crée ma liste à partir des paramètres saisis
    myList=numbers
    print(myList)

    # pour chaque valeur de ma liste, si le reste de ma valeur divisée par deux est égal à 0 
    # alors, l'afficher 
    for value in myList:
        if value%2 == 0:
            print(value)

fun(1, 2, 12, 25)





