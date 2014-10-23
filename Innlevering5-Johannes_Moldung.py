#Johannes Fåberg Moldung <johannes@moldung.no>

#Importerer grafisk og matematisk hjelpemidler
from graphics import*
from math import*
#DEL 1
#Beskrivelse av del 1
def G(w,t):
    return  1.2000+t*(1.8000-0.078*(log(w))-0.0946*(log(w))**2 +0.0105*(log(w))**3)
def vekt(w0,G,d):
    return w0*(1+G/100)**d
def relevant():
    while 4<=t<=14 and 0<=w<=600:
        return True

"""def badvekt(w0):
    return w0 > 600 or w0 < 0
def badtemp(t):
    return t < 4 or t > 14
def vindu(x):
    vindu = GraphWin("Feilmelding",1000,300)
    vindu.setCoords(1,1,5,5)
    tekst = Text(Point(3,3), "")
    tekst.draw(vindu)
    tekst.setText(str(x))
    klikk = vindu.getMouse()
    vindu.close()
def G(w0,t):
    return 1.2000 + t*(1.8000-0.078*log(w0) - 0.0946*(log(w0))**2 + 0.0105*(log(w0))**3)
def vekt(w0,G,d):
    return w0*(1+G/100)**d
def badday(w0,t,d):
    vekstrate = G(w0,t)
    vekten = vekt(w0,vekstrate,d)
    return badvekt(vekten)             
                
def maksdag(w0,t,d):
    vekstrate = G(w0,t)
    vekten = vekt(w0,vekstrate,d)
    for i in range(d):
        vekten = w0*(1+vekstrate/100)**i
        if badvekt(vekten):
            return i
def main():
    #vindu = GraphWin("Feilmelding",400,400)#flyttet ned hit
    #vindu.setCoords(0,0,5,5)# denne og
    #startvekt:
    d = 1000
    t = 0
    w0 = -1
    while badvekt(w0):
        w0 = eval(input("skriv inn startvekt i mg: "))
        if badvekt(w0):
            vindu("start-vekten må være mindre enn 600mg")
    while badtemp(t):
        t = eval(input("skriv inn temperatur i Celcius: "))
        if badtemp(t):
            vindu("temp må være mellom 4-14 C")
    while badday(w0,t,d):
        d = eval(input("skriv inn antall dager experimentet skal gå over: "))
        if badday(w0,t,d):
            vektdag = maksdag(w0,t,d)
            vindu("maksvekt passert ved dag "+str(vektdag))
    V = G(w0,t)
    Ve = vekt(w0,V,d)
    if not badvekt(w0) and not badtemp(t) and not badvekt(Ve):
        print("Vekten etter" , d , " dager, er:" , Ve , "mg")"""
    
#DEL 2.1
#Beskrivelse av del 2
def lagGUIvindu():
    #Setter opp grafikkvindu og koordinatsystem
    win = GraphWin("Codmandovindu", 400, 150)
    win.setBackground("white")
    win.setCoords(0,0,100,20)
    #Inputbokser
    #Rad 1
    #w0
    w0_txt = Text(Point(4,15),"w0")
    w0_txt.draw(win)
    #d
    d_txt = Text(Point(29,15),"d:")
    d_txt.draw(win)
    #t
    t_txt = Text(Point(54,15),"t:")
    t_txt.draw(win)
    #s
    s_txt = Text(Point(79,15),"s:")
    s_txt.draw(win)
    #Rad2
    #mw
    mw_txt = Text(Point(4,11),"mw:")
    mw_txt.draw(win)
    #N
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
#DEL 2.2
def oppvekst():
    #Sette opp nytt grafikkvindu
    win = GraphWin("Codmandovindu", 500, 500)
    win.setBackground("white")
    win.setCoords(-30,-30,380,380)
    #Sette opp synlig koordinatsystem
    rect = Rectangle(Point(0,0),Point(350,350))
    rect.setOutline("grey")
    rect.draw(win)
    for i in range[6]:
        lines = Line(Point(0,0),Point(0,0))
    return win
    
#MASTER FUNCTION
def main():
    #Run algorithm!^^
    inputwin = lagGUIvindu()
    #Definerer "Entry"
    #w0
    w0= Entry(Point(15,15),7)
    w0.draw(inputwin)
    #d
    d= Entry(Point(40,15),7)
    d.draw(inputwin)
    #t
    t= Entry(Point(65,15),7)
    t.draw(inputwin)
    #s
    s= Entry(Point(90,15),7)
    s.draw(inputwin)
    #mw
    mw= Entry(Point(15,11),7)
    mw.draw(inputwin)
    #N
    N= Entry(Point(40,11),7)
    N.draw(inputwin)
    #Setter avslutt til false for å kunne lukke while løkken ved å definere avsluttet til True
    #OK
    ok = Text(Point(95,2),'OK')
    ok.setOutline('green')
    ok.draw(inputwin)
    #vent
    vent = Text(Point(95,2),'vent')
    vent.setOutline('red')
    
    avslutt = False
    while not avslutt:
        p=inputwin.getMouse()
        p.x = p.getX()
        p.y = p.getY()
        w0_num = eval(w0.getText())
        d_num = eval(d.getText())
        t_num = eval(t.getText())
        s_num = eval(s.getText())
        mw_num = eval(mw.getText())
        N_num = eval(N.getText())
        if (p.x >= 10) and (p.x <= 30) and (p.y >= 3) and (p.y <= 7):
            ok.undraw()
            vent.draw(inputwin)
            print('w0:',w0_num,'d:',d_num,'t:',t_num,'s:',s_num,'mw:',mw_num,'N:',N_num)
            print(True)
            
            vent.undraw()
            ok.draw(inputwin)
        elif (p.x >= 35) and (p.x <= 55) and (p.y >= 3) and (p.y <= 7):
            print(True)
            oppvekst(w0,d,mw,t,s,TV)
        elif (p.x >= 60) and (p.x <= 80) and (p.y >= 3) and (p.y <= 7):
            inputwin.close()
            avslutt = True
        else:
            print(False)
