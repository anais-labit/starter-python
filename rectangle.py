nb_tirets=int(input("Quelle est la largeur du rectangle ? "))
nb_pipes=int(input("Quelle est la hauteur du rectangle ? "))

largeur=("-"*nb_tirets)
hauteur=("|"*nb_pipes)
espaces=(" "*nb_tirets)

i=2

while hauteur != nb_pipes:
    print("|" + largeur + "|")

    while i != nb_pipes :
        i +=1
        print("|" + espaces + "|")
        
    print("|" + largeur + "|")
    break


