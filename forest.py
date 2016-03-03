__author__ = 'Shweta Yakkali'
__author__ = 'Aishwarya Desai'

import turtle
import random

# global constants for window dimensions
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1600


def init():
    """
    Initialize for drawing.  (-800, -800) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (0,0), heading (north), up
    :post: pos (0,0), heading (north), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setx(-800)
    turtle.sety(-800)
    turtle.title('Forest')
    turtle.speed(1)

def drawTrunk(length):
    """
    Draw the Trunk.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (north), up
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.down()
    turtle.forward(length)

def drawPine(length):
    """
    Draw the Pine Tree.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (south), up
    :return: None
    """
    turtle.right(90)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(30)
    turtle.up()
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(100)


def drawMaple(length):
    """
    Draw the Maple Tree.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (south), up
    :return: None
    """
    turtle.down()
    turtle.right(90)
    turtle.circle(25.9)
    turtle.up()
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(100)


def drawThird(length):
    """
    Draw a 3rd tree of our choice.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (south), up
    :return: None
    """
    turtle.right(45)
    turtle.forward(36.7)
    turtle.left(90)
    turtle.forward(36.7)
    turtle.left(90)
    turtle.forward(36.7)
    turtle.left(90)
    turtle.forward(36.7)
    turtle.up()
    turtle.right(45)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(100)

def star():
    """
    Draws a star which starts at a position of 10 pixels higher than the tallest tree+ 52, where
    52 is the height of the equilateral triangle in pine or diameter of circle in maple or diagonal of rhombus in 3rd tree.
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (south-east), up
    :return: None
    """
    
    global maxht

    turtle.setx(-600)
    turtle.sety(-(728-10-maxht)) #to print the star 10pixels higher than the tallest tree

    turtle.down()
    turtle.forward(5)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(5)
    turtle.right(45)
    turtle.forward(5)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(5)

def House(height,side):
    """
    Draw the House.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (south), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(45)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(45)
    turtle.forward(height)
    turtle.left(90)
    turtle.up()
    turtle.forward(100)

def drawSun():
    """
    Draw the Sun.
    :pre: (relative) pos (0,0), heading (eat), up anticlockwise
    :post: (relative) pos (0,0), heading (west), up
    :return: None
    """
    turtle.up()
    turtle.sety(400)
    turtle.setx(400)
    turtle.down()
    turtle.circle(20)

def drawRanTree(woods):
    """
    Draw the Trees which are random.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (south), up
    :return: None
    """
    l=0
    length=0
    global wood
    global maxht
    l=random.randint(1,3)

    if l==1:
        length=random.randint(50,200)
        if(maxht<length):
              maxht=length
        x=length
        wood=wood+length
        print("l=1",wood)
        drawTrunk(length)
        drawPine(length)

    elif l==2:
        length=random.randint(50,150)
        if(maxht<length):
              maxht=length
        y=length
        wood=wood+length
        print("l=2",wood)
        drawTrunk(length)
        drawMaple(length)

    elif l==3:
        length=random.randint(50,100)
        if(maxht<length):
              maxht=length
        z=length
        wood=wood+length
        print("l=3",wood)
        drawTrunk(length)
        drawThird(length)

    return wood

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (south-east), up
    :return: None
    """
    init()
    global wood
    global maxht
    global totalwood
    wood=0
    maxht=0
    totalwood=0
    n=0

    #scene=int(input("Do you want a day scene or night scene enter 1 for night and zero for day?"))


    n=int(input("How many trees do you want in the forest ? "))
    house=int(input("do you want a house? yes=1/no=0 : "))
    a=random.randint(1,(n-1))

    for i in range(n):

        if (a==i and house==1):
            House(100,71)

        woodoftrunk=drawRanTree(wood)
    #print("max height=",maxht)
    star()
    woodofhouse=100+71+71+100
    totalwood=woodoftrunk+woodofhouse
    print("total wood=",totalwood)
    input("night is done press enter for day")

    turtle.reset()
    print("we have",totalwood,"units of lumber for building")
    height=totalwood/(2+1.414)
    print("we will build a house with walls",height,"tall")
    side=height/1.414
    House(height,side)
    drawSun()
    input("day is done,house is built,press enter to quit!")


input('Hit enter ')
turtle.bye()


if __name__ == '__main__':
    main()