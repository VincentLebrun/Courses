age = int(input("Quel est votre age?"))
username = input('Quel est le nom de votre héros?')

while 1:
    sexe = input("Choisissez le sexe de votre personnage en tapant M pour Masculin et F pour féminin.")
    if sexe in ( "F" , "M", "f","m"):
        break
    else:
        print("Faites un choix bon sang!")

user_choice = int(input("Choisissez votre classe parmi les suivantes ""1=Humain 2=Elfe 3=Orque 4=Troll"))
if   user_choice == 1:
    race = "Humain"
elif user_choice == 2:
    race = "Elfe"
elif user_choice == 3:
    race = "Orque"
elif user_choice == 4:
    race = "Troll"
else:
    print("Il n'y a que 4 choix c'est pourtant pas compliqué!")

print(username,"Vous avez rejoint la race des ", race, "dans un petit village nommé Rakda")

