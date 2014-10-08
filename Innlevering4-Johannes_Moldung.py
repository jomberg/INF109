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
    if ikketom(line[56:59]):
        return eval(line[56:59])
    elif ikketom(line[63:67]):
        return eval(line[63:67])
    elif ikketom(line[71:75]):
        return eval(line[71:75])

#PART 1.3
def relevant(longtitude, latitude, x1, y1, x2, y2):
    if x1<=longtitude<=x2 and y1<=latitude<=y2:
        return True
    else:
        return False

#PART 2
def tegnJordskjelv(window, longtitude, latitude, styrke, x1, y1, x2, y2):
    #Define window for drawing earthquake
    earthquake_point = Circle(Point(longtitude,latitude),styrke)
    #window.setCoords(-180,-90,180,90) #To fit the earth's positioning system
    window.setCoords(x1,y1,x2,y2) #To fit the earth's positioning system
    earthquake_point.setOutline ("purple")
    earthquake_point.draw(window)

#PART 3
def Mo(M): #Shall calculate seismic moment rate in newton-meters per year
    return 10**((1.5 * M) + 9.1)
    
#MASTER FUNCTION
def main():
    #Get filename from user
    file = input("File name + file type = ?")
    #Get coordinates from user
    x1 = eval(input('Coordinate for "X1" in square= ? '))
    x2 = eval(input('Coordinate for "X2" in square= ? '))
    y1 = eval(input('Coordinate for "Y1" in square= ? Y2 will be calculated for you.'))
    y2 = y1+0.5*(x2-x1)
    print("\n")
       
    usr_file = open(file,'r')
    #Window for earthquake
    window = GraphWin("Earthquake File={} x1={} y1={} x2={} y2={}".format(file,x1,y1,x2,y2), 800, 400)

    antall_skjelv = sum_seismisk_moment = 0
    start_aar = 9999
    slutt_aar = 0
    min_magn = 9999
    max_magn = 0
    window_margin = 3
    usr_file = open(file,'r')
    for line in usr_file.readlines():
        if godlinje(line) == True and len(line) != 0:
            latitude = eval(line[23:29])
            longtitude = eval(line[30:37])
            if relevant(longtitude, latitude, x1, y1, x2, y2)== True:
                #print (line)
                magnitude = (styrke(line))
                min_magn = min(magnitude,min_magn)
                max_magn = max(magnitude,max_magn)
                #print (magnitude)
                #tegnJordskjelv(window, longtitude, latitude, magnitude/10, x1-window_margin, y1-window_margin, x2+window_margin, y2+window_margin)
                sum_seismisk_moment = sum_seismisk_moment + Mo(magnitude)
                antall_skjelv += 1
            if ikketom(line[1:5]) == True:
                year = eval(line[1:5])
                slutt_aar = max(slutt_aar, year)
                start_aar = min(start_aar, year)
    # slutt, regn ut total seismisk moment: =sum_seismisk_moment/antall_aar
    antall_aar = slutt_aar - start_aar
    seismisk_momentrate = sum_seismisk_moment / (slutt_aar - start_aar)

    #PART 4
    # rapporter funn
    print ("\nKoordinater for omraade: (%.3f,%.3f) og (%.3f,%.3f)" %(x1,y1,x2,y2))
    print("EQ-katalog: {}".format(file))
    print("Katalogen dekker perioden %d-%d (%d aar)" %(start_aar,slutt_aar,antall_aar))
    print("Antall jordskjelv:", antall_skjelv)
    print("Minimum magnitude: %.2f, max magnitude: %.2f" %(min_magn, max_magn))
    print("Totalt seismisk moment: %.11e Nm" %(sum_seismisk_moment))
    print("Seismisk momentrate: %.11e Nm/aar" %(seismisk_momentrate))

main()
