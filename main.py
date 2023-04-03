import personbil
import lastbil

looping = True

volvo_red =  personbil.Personbil("Volvo", "röd", 200)
opel_red = personbil.Personbil("Opel", "röd", 250)
ferrari_gul = personbil.Personbil("Ferrari", "gul", 30)

scania_blue = lastbil.Lastbil("Scania", "blå", 3440)
volvo_gray = lastbil.Lastbil("Volvo", "grå", 34333)

#skapar listor med fordon
personbils_lista = [volvo_red, opel_red, ferrari_gul]
lastbils_lista = [scania_blue, volvo_gray]

def print_fordonslista(fordonslista):

    for ett_fordon in fordonslista:
        if (isinstance (ett_fordon, lastbil.Lastbil)):
            print(ett_fordon.fabrikat + "Färg: " + ett_fordon.color + ", FlakV: " + str(ett_fordon.flakvolym) + " Ton")

        elif (isinstance (ett_fordon, personbil.Personbil)):
            print(ett_fordon.fabrikat + "Färg: " + ett_fordon.color + ", Bagagevolym: " + str(ett_fordon.bagagevolym) + " L")
    

while looping:

    val_av_fordon = input("Vilken fordonstyp väljer du? 1 = Lastbilar eller 2 = Personbilar -> ")

    if(val_av_fordon == "1"):
        print("\nLista med lastbilar")
        print("----------------------------------")
        print_fordonslista(lastbils_lista)

    elif(val_av_fordon == "2"):
        print("\nLista med personbilar")
        print("----------------------------------")
        print_fordonslista(personbils_lista)
    

    go = input("\n Vill du lista fordon igen? j/n ")
    print("\n")

    print("---------------------------------------------------------------------------------")
    print("\nKlasser och arv ")

    #------------------------------------------------------------------------------------------------
    

    if (go == "n"):
        break