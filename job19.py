def fun(*numbers):
    
    #créer une liste vide 
    myList = []                                                 

    # pour chaque nombre saisi en paramètre, l'enregistrer dans la liste :
    for number1 in numbers:
        myList.append(number1)                                        

    # pour chaque number1 dans la longueur de la liste, et chaque number2 +1, si number1 > number2, remplacer l'ordre des deux :
    for number1 in range(len(myList)):                                
        for number2 in range(number1 + 1, len(myList)):
            if myList[number1] > myList[number2]:                           
                myList[number1], myList[number2] = myList[number2], myList[number1]  

    print("Mes chiffres par odre croissant :"  + str(myList))

fun(1, 3, 4, 7, 9, 7, 56, 32)

