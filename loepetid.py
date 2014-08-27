#dette programmet skal regne ut den samlede poengsummen for løpene, hvor brukeren fyller tiden, og distansen for hvert løp

def sammenlagt():
    #her legger vi inn bruker-definisjon for navn
    navn =(input("Navn: "))
    #første løp
    print("Første løp")
    dist1 = eval(input("Distanse: "))
    tid_min1 = eval(input("Minutter: "))
    tid_sek1 = eval(input("Sekunder med komma: "))
    
    #andre løp
    print("Andre løp")
    dist2 = eval(input("Distanse: "))
    tid_min2 = eval(input("Minutter: "))
    tid_sek2 = eval(input("Sekunder med komma: "))
    
    #tredje løp
    print("Tredje løp")
    dist3 = eval(input("Distanse: "))
    tid_min3 = eval(input("Minutter: "))
    tid_sek3 = eval(input("Sekunder med komma: "))
    
    #fjerde løp
    print("Fjerde løp")
    dist4 = eval(input("Distanse: "))
    tid_min4 = eval(input("Minutter: "))
    tid_sek4 = eval(input("Sekunder med komma: "))
    
    #let the math-madness begin
    L_1 = ((tid_min1*60)+tid_sek1)/(dist1/500)
    L_2 = ((tid_min2*60)+tid_sek2)/(dist2/500)
    L_3 = ((tid_min3*60)+tid_sek3)/(dist3/500)
    L_4 = ((tid_min4*60)+tid_sek4)/(dist4/500)
    P = L_1+L_2+L_3+L_4
    #let the pinting comense

    #print av løp1
    print("Navn: ",navn)
    print("Tid for ",navn,"på",dist1,"meter")
    print("Minutter:",tid_min1,"\nSekunder og hundredeler:",tid_sek1)
    #print av løp2
    print("Tid for ",navn,"på",dist2,"meter")
    print("Minutter:",tid_min2,"\nSekunder og hundredeler:",tid_sek2)
    #print av løp3
    print("Tid for ",navn,"på",dist3,"meter")
    print("Minutter:",tid_min3,"\nSekunder og hundredeler:",tid_sek3)
    #print av løp4
    print("Tid for ",navn,"på",dist4,"meter")
    print("Minutter:",tid_min4,"\nSekunder og hundredeler:",tid_sek4)
    #print av salet poengsum
    print("Den samlede poengsummen til",navn,":",(round(P,3)))
#her på slutten kaller jeg på definisjonen slik at når programmet kjøres så går det rett til å spørre om bruker-input, uten å måtte kalle det i shellet først
sammenlagt()
#note to self:høy poengsum=dårlig prestasjon, lav poengsum=god prestasjon
