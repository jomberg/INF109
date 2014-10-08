#Johannes Fåberg Moldung <johannes@moldung.no>

#Import mathematicl and graphical help
from graphics import*
from math import*

#MASTER FUNCTION
def earthquake():
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
    #
    usr_file = open(file,'r')
    for line in usr_file.readlines():
        if goodline(line) == True and len(line) != 0:
            latitude = eval(line[23:29])
            longtitude = eval(line[30:37])
            if relevant(longtitude, latitude, x1, y1, x2, y2)== True:
                usr_file = open(file,'r')

                magnitude = (strength(line))
                
                drawEarthquake(window, longtitude, latitude, magnitude/10)

    usr_file = open(file, 'r')
    top = 0
    bottom = 9999#Reason
    for line in usr_file:
        if notempty(line[1:5]) == True:
            year = eval(line[1:5])
            if year > top:
                top = year
            if year < bottom:
                bottom = year
    differance = top - bottom

    
            
#PART 1.1
def notempty(string):
    return string.strip() != ''
def goodline(line):
    if notempty(line[23:29]) != False and notempty(line[30:37]) != False:
        return True
#PART 1.2
def strength(line):
    if notempty(line[56:58]):
        return eval(line[56:58])
    elif notempty(line[63:66]):
        return eval(line[63:66])
    elif notempty(line[71:74]):
        return eval(line[71:74])
#PART 1.3
def relevant(longtitude, latitude, x1, y1, x2, y2):
    if x1<=longtitude<=x2 and y1<=latitude<=y2:
        return True
    else:
        return False
#PART 2
def drawEarthquake(window, longtitude, latitude, strength):
    #Define window for drawing earthquake
    earthquake_point = Circle(Point(longtitude,latitude),strength)
    window.setCoords(-180,-90,180,90)#To fit the earth's positioning system
    earthquake_point.setOutline ("purple")
    earthquake_point.draw(window)
#PART 3
def M0(M):#Shall calculate seismic moment rate in newton-meters per year

#PART 4
    
earthquake()
