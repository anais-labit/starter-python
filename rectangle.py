nb_tirets=int(input("Quelle est la largeur du rectangle ? "))
nb_pipes=int(input("Quelle est la hauteur du rectangle ? "))

largeur=("-"*nb_tirets)
hauteur=("|"*nb_pipes)
espaces=(" "*nb_tirets)

i=2

# haut : tant que la hauteur ne correspond au nb_pipes voulu, fais | nb_tirets | 
while hauteur != nb_pipes:
    print("|" + largeur + "|")

    # corps : et tant que i ne correspond pas au nb_pipes, fais | nb_espaces | sur toutes les lignes
    while i != nb_pipes :
        i +=1
        print("|" + espaces + "|")

# base : quand la hauteur correspond au nb_pipes voulu, fais | nb_tirets |
    print("|" + largeur + "|")
    break
