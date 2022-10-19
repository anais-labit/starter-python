hauteur=int(input("Quelle sera la hauteur des cotés du triangle ? "))

top=("."*hauteur)

# pour i allant de 0 à 6 (soit "hauteur")
for i in range(hauteur):

    left=(" "*(hauteur-i))
    middle=(" "*(2*i))
    base=("_"*(2*i))

    # si i est égal hauteur, supprime un espace et fais / base \ 
    if i == (hauteur-1):
        print(" /" + base + "\\")

    # sinon, supprime un espace et fais / middle \
    else:
        print(left + "/" + middle + "\\")
