import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "ho ho ho merry bidmas"

satellites = []
lines = []

start_time = 0
total_time = 0
end_time = 0

no_of_satellites = 10

def create_sats():
    global start_time , no_of_satellites
    for hi in range(no_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = random.randint(40, 750),random.randint(40,750)
        satellites.append(satellite)
        
