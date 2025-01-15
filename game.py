import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "ho ho ho merry bidmas"

satellites = []
lines = []
current_satellite = 0
start_time = 0
total_time = 0
end_time = 0

no_of_satellites = 10

def create_sats():
    global start_time , no_of_satellites
    for hi in range(no_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40,750),randint(40,550)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    num = 1
    for satellite in satellites:
        screen.draw.text(str(num),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        num += 1
    for i in lines:
        screen.draw.line(i[0],i[1],(255,255,255))
    if current_satellite < no_of_satellites:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)

def update():
    pass

def on_mouse_down(pos):
    global current_satellite, lines
    if current_satellite < no_of_satellites:
        if satellites[current_satellite].collidepoint(pos):
            if current_satellite:
                


    


create_sats()
pgzrun.go()
