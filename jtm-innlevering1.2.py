#!/usr/bin/python3

# UiB INF109 høsten 2014 innleveringsoppgave 1 del 2
# Johannes Fåberg Moldung <johannes@moldung.no>

# Dette programmet skal regne ut den samlede poengsummen for løpene, hvor
# brukeren fyller tiden, og distansen for hvert løp

def sammenlagt():
    #her legger vi inn bruker-definisjon for navn
    navn =(input("Navn: "))

    # Definer en liste med distansene
    distanser = [ 500, 5000, 1500, 10000 ]

    # Poeng-teller, settes lik 0
    poeng = 0

    # Løp over verdiene i listen distanser, i løkke
    for distanse in distanser:
        print ("Tid for " + navn + " på " + str(distanse) + " meter: ")
        minutter = eval(input("Minutter: "))
        sekunder = eval(input("Sekunder og hundrededeler: "))
        poeng = poeng + ( ( (minutter*60) + sekunder) / (distanse / 500 ) )
    print ("Sammenlagt poengsum for " + navn + " : " + str(round(poeng,3)) )

# Her på slutten kaller jeg på definisjonen slik at når programmet kjøres
# så går det rett til å spørre om bruker-input, uten å måtte kalle det
# i shellet først
sammenlagt()

# Note to self:høy poengsum=dårlig prestasjon, lav poengsum=god prestasjon
