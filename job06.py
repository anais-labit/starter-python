answer=input("> ")

while True:

    if answer == "Bonjour":
        print("Bonjour à toi !")
        answer=input("> ")

    elif answer == "Au revoir":
        print("exiting the program")
        exit
        break

    else:
        answer=input("> ")
        break
