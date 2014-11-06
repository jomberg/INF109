#Johannes Fåberg Moldung - jmo015

#Importerer grafisk og matematisk hjelpemidler
from graphics import*
from math import*
from random import*

def G(w,t):
    return  1.2000+t*(1.8000-0.078*(log(w))-0.0946*(log(w))**2 +0.0105*(log(w))**3)
def vekt(w,t,G,d,s):
    X = gauss(1,s)
    for n in range(d):
        X = (X+gauss(1,s))/2
        xg = G(w,t)
        ans = w*(1+((xg)/100))
        return ans

def relevant(t,mw):
    while 4<=t<=14 and 0<=mw<=600:
        return True    

def lagGUIvindu():
    #Setter opp grafikkvindu og koordinatsystem
    win = GraphWin("Codmandovindu", 400, 150)
    win.setBackground("white")
    win.setCoords(0,0,100,20)
    #Inputbokser
    w0_txt = Text(Point(4,15),"w0")
    w0_txt.draw(win)
    d_txt = Text(Point(29,15),"d:")
    d_txt.draw(win)
    t_txt = Text(Point(54,15),"t:")
    t_txt.draw(win)
    s_txt = Text(Point(79,15),"s:")
    s_txt.draw(win)
    mw_txt = Text(Point(4,11),"mw:")
    mw_txt.draw(win)
    N_txt = Text(Point(29,11),"N:")
    N_txt.draw(win)
    #Knapper
    #Calculation button
    calc_but = Text(Point(20,5),"Beregning")
    calc_but.draw(win)
    calc_rect = Rectangle(Point(10,3),Point(30,7))
    calc_rect.draw(win)
    #New button
    new_but = Text(Point(45,5),"Ny Figur")
    new_but.draw(win)
    new_rect = Rectangle(Point(35,3),Point(55,7))
    new_rect.draw(win)
    #Quit
    q_but = Text(Point(70,5),"Avslutt")
    q_but.draw(win)
    q_rect = Rectangle(Point(60,3),Point(80,7))
    q_rect.draw(win)
    return win

def grafvindu(d,mw):
    #Sette opp nytt grafikkvindu
    win = GraphWin("Codmandovindu-Graf", 500, 500)
    win.setBackground("white")
    win.setCoords(-(d)*0.2,-(mw)*0.2,(d)*1.2,(mw)*1.2)#+- 35 for marg
    #Sette opp synlig koordinatsystem
    #Firkant
    rect = Rectangle(Point(0,0),Point(d,mw))
    rect.draw(win)
    #Aksetekst
    x_axis = Text(Point((d)/2,0-(mw)*0.05),"DAGER")
    x_axis.draw(win)
    y_axis = Text(Point(0-(d)*0.09,(mw)/2),"VEKT")
    y_axis.draw(win)

    return win

def graftegn(w0,d,mw,t,s,TV):
    #Indikatorlinjer
    for i in range(6):
        #Setter opp variabler for bruk i tegning av punkter
        inc_x = 0+(i*(d/5))
        inc_y = 0+(i*(mw/5))
        stat_0 = 0
        stat_x = d
        stat_y = mw
        #Tegner punkter
        #Nedre x-akse
        low_line = Line(Point(inc_x,(stat_0)-((mw)*0.02)),Point(inc_x,(stat_0)+((mw)*0.02)))
        low_line.draw(TV)
        #Øvre x-akse
        up_line = Line(Point(inc_x,(stat_y)-((mw)*0.02)),Point(inc_x,(stat_y)+((mw)*0.02)))
        up_line.draw(TV)
        #Venstre y-akse
        left_line = Line(Point((stat_0)-((d)*0.02),inc_y),Point((stat_0)+((d)*0.02),inc_y))
        left_line.draw(TV)
        #Høyre y-akse
        right_line = Line(Point((stat_x)-((d)*0.02),inc_y),Point((stat_x)+((d)*0.02),inc_y))
        right_line.draw(TV)
        #Tall ved indikatorlinjene
        x_num1 = Text(Point(inc_x,-stat_y*0.09),"{}".format(int(inc_x)))
        x_num1.draw(TV)
        x_num2 = Text(Point(inc_x,stat_y*1.09),"{}".format(int(inc_x)))
        x_num2.draw(TV)
        y_num1 = Text(Point(-stat_x*0.09,inc_y),"{}".format(int(inc_y)))
        y_num1.draw(TV)
        y_num2 = Text(Point(stat_x*1.09,inc_y),"{}".format(int(inc_y)))
        y_num2.draw(TV)

def oppvekst(w0,d,mw,t,s,TV):
    print(t)
    d=int(d)
    w=w0
    w1=Point(0,0)
    w2=Point(0,0)
    for k in range(d):
        if w<mw:
            w = vekt(w,t,G,d,s)
            w1 = Point(1+k,w)
            tlinje = Line(w1,w2)
            tlinje.setWidth(3)
            tlinje.setOutline('blue')
            tlinje.draw(TV)
            w2 = w1
    
#MASTER FUNCTION
def main():
    #Run algorithm!^^
    inputwin = lagGUIvindu()
    #Definerer "Entry"
    w0_usr = Entry(Point(15,15),7)
    w0_usr.draw(inputwin)
    d_usr = Entry(Point(40,15),7)
    d_usr.draw(inputwin)
    t_usr = Entry(Point(65,15),7)
    t_usr.draw(inputwin)
    s_usr = Entry(Point(90,15),7)
    s_usr.draw(inputwin)
    mw_usr = Entry(Point(15,11),7)
    mw_usr.draw(inputwin)
    N_usr = Entry(Point(40,11),7)
    N_usr.draw(inputwin)
    #Setter opp tekstfelt i vinduet som sier om vinduet er klar til bruk
    ok = Text(Point(95,2),'OK')
    ok.setOutline('green')
    ok.draw(inputwin)
    vent = Text(Point(95,2),'vent')
    vent.setOutline('red')
    #Setter opp varible til bruk senere
    first = 1
    #Setter avslutt til false for å kunne lukke while løkken ved å definere avsluttet til True
    avslutt = False
    while not avslutt:
        p=inputwin.getMouse()
        p.x = p.getX()
        p.y = p.getY()
        if (p.x >= 10) and (p.x <= 30) and (p.y >= 3) and (p.y <= 7):
            #Forteller brukeren at programmet jobber
            ok.undraw()
            vent.draw(inputwin)
            #Henter ut nyeste brukerinput som tall
            w0 = float(w0_usr.getText())
            d = float(d_usr.getText())
            t = float(t_usr.getText())
            s = float(s_usr.getText())
            mw = float(mw_usr.getText())
            N = float(N_usr.getText())
            #Sjekker om data fra brukeren er innenfor den amtematiske modellen
            if relevant(t,mw) == True:
                #Sjekker om det er det eneste vinduet ved hjelp av varibel definert utenfor løkken
                if first > 0:
                    TV = grafvindu(d,mw)
                graftegn(w0,d,mw,t,s,TV)
                oppvekst(w0,d,mw,t,s,TV)
                
                #Omdefinerer variabelen så løkken ikke lager flere vindu
                first = 0
                #Forteller brukeren at programmet er ferdig
                vent.undraw()
                ok.draw(inputwin)
            else:
                print("ugyldig data!")
                vent.undraw()
                ok.draw(inputwin)
        elif (p.x >= 35) and (p.x <= 55) and (p.y >= 3) and (p.y <= 7):
            #Forteller brukeren at programmet jobber
            #Forteller brukeren at programmet jobber
            ok.undraw()
            vent.draw(inputwin)
            #Sjekker om det er det eneste vinduet, og lukker de eventuelle andre vinduene
            if first == 0:
                TV.close()
            #Henter ut nyeste brukerinput som tall
            w0 = float(w0_usr.getText())
            d = float(d_usr.getText())
            t = float(t_usr.getText())
            s = float(s_usr.getText())
            mw = float(mw_usr.getText())
            N = float(N_usr.getText())
            TV = grafvindu(d,mw)
            graftegn(w0,d,mw,t,s,TV)
            oppvekst(w0,d,mw,t,s,TV)
            #Omdefinerer variabelen så løkken ikke lager flere vindu
            first = 0
            #Forteller brukeren at programmet er ferdig
            vent.undraw()
            ok.draw(inputwin)
        elif (p.x >= 60) and (p.x <= 80) and (p.y >= 3) and (p.y <= 7):
            if first == 0:
                TV.close()
            inputwin.close()
            avslutt = True

main()
