"""
Coding challenge 002 "Menger Sponge"
Created in Processing 3.5.4 with Python mode
Author: Maksim Kurchevskiy
Patreon: https://patreon.com/thienxxn

Motivated by: Daniel Shiffman
Original code was shown in: https://youtu.be/LG8ZK-rRkXo
"""

# define screen constants
WINDOW_WIDTH = 800  # define window width
WINDOW_HEIGHT = 600 # define window height 

CUBE_SIZE = 250  # set another value for this const, if u want to change size of start cube

# define some global variables
sponge = list()     # this list keeps all boxes
angle = 0           # this var uses for scene rotation



# this function works on sketch set up
def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT, P3D)  # creating a window with a P3D renderer
    
    # creating first box and add it to 'sponge' list
    startBox = Box(0,0,0, CUBE_SIZE)
    sponge.append(startBox)


# this function calls every frame
def draw():
    global angle  # say, that we need angle variable as global, not local
    
    background('#F2F8FF') # Set backound color
    translate(width / 2, height / 2) # set viewpoint to the center of screen
    noFill()  # saying we dont need to fill anything
    lights()  # adding some lights on scene

    # here we just rotating our scene on some angle
    # we also need to increment our angle ofc
    rotateY(angle)
    rotateX(angle*0.6)
    angle += 0.01
    
    # just drawing all boxes from sponge
    for box_ in sponge:
        box_.show()


# when user press mouse left key, this function calls out
def mousePressed():
    global sponge # saying, that we need to use sponge
    
    # we need another list for saving next generation
    newSponge = list() 
    
    # for each box in sponge we calls nextGeneration() func
    for _box in sponge:
        nextGen = _box.nextGeneration()
        
        # now we have some lists in nextGen, so we need to add them
        # all to the newSponge not as lists, but as Boxes
        for newBox in nextGen:
            newSponge.append(newBox)
    
    sponge = newSponge


# class for every box on screen
class Box():
    # define constructor
    def __init__(self, x, y, z, r):
        """
        x, y, z : coordinates of box on screen (starting at center)
        r : size of box (im using r instead of size, because size is a special word in Processing)
        """
        self.pos = PVector(x,y,z)
        self.r = r
    
    # function for draw box on screen
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        noStroke()
        fill('#FFFA93')
        box(self.r)
        popMatrix()
    
    def nextGeneration(self):
        boxes = list() # boxes for saving new boxes result
        
        # so, we need to chop our box into small boxes,
        # but delete all center pieces
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    sum = abs(x) + abs(y) + abs(z)
                    
                    # size of box should be size / 3
                    newSize = float(self.r / 3)
                    
                    # if sum > 1, than we not at center
                    # and can just not to draw this box
                    if(sum > 1):
                        b = Box(self.pos.x + x * newSize,
                                self.pos.y + y * newSize,
                                self.pos.z + z * newSize,
                                newSize)
                        
                        boxes.append(b)
        
        return boxes # returning next generation
