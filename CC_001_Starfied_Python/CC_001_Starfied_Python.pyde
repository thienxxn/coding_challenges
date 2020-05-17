"""
Coding challenge 001 "StarField"
Created in Processing 3.5.4 with Python mode
Author: Maksim Kurchevskiy
Patreon: https://patreon.com/thienxxn

Inspired by: Daniel Shiffman
Original code was shown in: https://youtu.be/17WoOqgXsRM
"""


# define some constants i will use
STAR_COUNT = 500  # this constant show, how much stars will be created
STAR_SPEED = 15   # this constant show, speed of every star

WINDOW_WIDTH = 600  # define window width
WINDOW_HEIGHT = 600 # define window height 

stars = list()  # creating an empty list for stars, we will add them in future


# this method works on program start 
def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT)  # creating a window
    background(0)  # set black color as background
    
    # fill our stars list with stars
    for i in range(STAR_COUNT):
        stars.append(Star())


# this method draw some stuff on screen every frame
def draw():
    background(0)  # set black color as background
    translate(width / 2, height / 2)  # change viewpoint to the center

    # iterating throught the stars
    for star in stars:
        star.update()  # update each star location
        star.display() # display each star


# creating Star class
class Star:

    def __init__(self):
        # random position for each star
        self.x = random(-width, width)
        self.y = random(-height, height)
        # i will move every star with the 'z' by dividing on this z
        self.z = random(width)
        
        # pz - its a previous z
        self.pz = self.z

    def update(self):
        # update the z with STAR_SPEED
        self.z -= STAR_SPEED
        
        # if our star moving out from screen
        # then we need to update this position
        if self.z < 1:
            self.x = random(-width, width)
            self.y = random(-height, height)
            self.z = random(width)
            self.pz = self.z
    
    # method for draw Star
    def display(self):
        noStroke()  # set up noStroke() that removing outline
        fill(255)   # set up fill color as white
        
        # calculating new coordintates for star
        sx = map(self.x / self.z, 0, 1, 0, width / 2)
        sy = map(self.y / self.z, 0, 1, 0, height / 2)

        px = map(self.x / self.pz, 0, 1, 0, width / 2)
        py = map(self.y / self.pz, 0, 1, 0, height / 2)
        
        # code below will display stars as a circles with 'tails'
        # but without this code, its just about 'tails'
        
        # r = map(self.z, 0, width, 8, 0)
        # circle(sx, sy, r)
        
        #set up previous z as z
        self.pz = self.z
        
        # draw a 'tail' of a star
        stroke(255)
        line(sx, sy, px, py)
