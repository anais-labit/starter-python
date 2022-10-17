nb1=int(input("Choisis un nombre entre 0 et 10 : "))
nb2=int(input("Choisis un deuxième nombre entre 0 et 10 : "))

if nb1 == nb2:
    print("Valeurs égales")

elif nb1 < nb2:
    for i in range(nb1+1, nb2):
        print(i)

elif nb1 > nb2:
    for i in range(nb1-1, nb2, -1):
        print(i)
