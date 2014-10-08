#Johannes Fåberg Moldung <johannes@moldung.no>

#Import mathematicl and graphical help
from graphics import*
from math import*

#PART 1.1
def ikketom(string):
    return string.strip() != ''

def godlinje(line):
    if ikketom(line[23:29]) != False and ikketom(line[30:37]) != False:
        return True

#PART 1.2
def styrke(line):
    if ikketom(line[56:58]):
        return eval(line[56:58])
    elif ikketom(line[63:66]):
        return eval(line[63:66])
    elif ikketom(line[71:74]):
        return eval(line[71:74])

#PART 1.3
def relevant(longtitude, latitude, x1, y1, x2, y2):
    if x1<=longtitude<=x2 and y1<=latitude<=y2:
        return True
    else:
        return False

#PART 2
def tegnJordskjelv(window, longtitude, latitude, styrke):
    #Define window for drawing earthquake
    earthquake_point = Circle(Point(longtitude,latitude),styrke)
    window.setCoords(-180,-90,180,90) #To fit the earth's positioning system
    earthquake_point.setOutline ("purple")
    earthquake_point.draw(window)

#PART 3
def Mo(M): #Shall calculate seismic moment rate in newton-meters per year
    return 10**(1.5 * M + 9.1)
    
#MASTER FUNCTION
def main():
    #Get filename from user
    file = input("File name + file type = ?")
    #Get coordinates from user
    x1 = eval(input('Coordinate for "X1" in square= ? '))
    x2 = eval(input('Coordinate for "X2" in square= ? '))
    y1 = eval(input('Coordinate for "Y1" in square= ? Y2 will be calculated for you.'))
    y2 = y1+0.5*(x2-x1)
       
    usr_file = open(file,'r')
    #Window for earthquake
    window = GraphWin("Earthquake File={} x1={} y1={} x2={} y2={}".format(file,x1,y1,x2,y2), 800, 400)

    antall_skjelv = sum_seismisk_moment = 0
    start_aar = 9999
    slutt_aar = 0
    usr_file = open(file,'r')
    for line in usr_file.readlines():
        if godlinje(line) == True and len(line) != 0:
            latitude = eval(line[23:29])
            longtitude = eval(line[30:37])
            if relevant(longtitude, latitude, x1, y1, x2, y2)== True:
                magnitude = (styrke(line))
                tegnJordskjelv(window, longtitude, latitude, magnitude/10)
                sum_seismisk_moment = sum_seismisk_moment + Mo(magnitude)
                antall_skjelv += 1
                if ikketom(line[1:5]) == True:
                    year = eval(line[1:5])
                    slutt_aar = max(slutt_aar, year)
                    start_aar = min(start_aar, year)
    # slutt, regn ut total seismisk moment: =sum_seismisk_moment/antall_aar
    seismisk_momentrate = sum_seismisk_moment / (slutt_aar - start_aar)

    #PART 4
    # rapporter funn
    print("Koordinater for omraade: ({},{}) og ({},{})".format(x1,y1,x2,y2) )
    print("EQ-katalog: {}".format(file))
    print("Katalogen dekker perioden ", start_aar, "-", slutt_aar)
    print("Antall jordskjelv: ", antall_skjelv)
    print("Totalt seismisk moment: ", sum_seismisk_moment, " Nm")
    print("Seismisk momentrate: ", seismisk_momentrate, " Nm/aar")

main()
