__author__ = 'shweta yakkali'
import turtle

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init(numbr):
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-200,-200,
        200,200)
    turtle.up()
    turtle.setheading(0)

    turtle.title('Name')
    turtle.speed(1)


    turtle.setx(numbr+30)
    turtle.sety(100)

def drawS():
    """
     Draws the letter 'S'
     :pre: pos (relative), lower left initial position of letter S, heading (east),up
     :post: pos (relative), upper right final position of letter S heading (east), up
     :return: None
    """


    turtle.down()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    pass

    turtle.up()

def drawH():
    """
     Draws the letter 'H'
     :pre: pos (relative), lower left initial position of letter H, heading (north),up
     :post: pos (relative), lower left final position of letter H heading (south), up
     :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(40)
    pass

    turtle.up()

def drawW():
    """
     Draws the letter 'W'
     :pre: pos (relative), lower left initial position of letter W, heading (north),up
     :post: pos (relative), upper right final position of letter W heading (north), up
     :return: None
    """


    turtle.down()
    turtle.left(180)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(40)
    turtle.left(135)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(135)
    turtle.forward(40)
    pass

    turtle.up()

def drawY():
    """
     Draws the letter 'Y'
     :pre: pos (relative), lower left initial position of letter Y, heading (north),up
     :post: pos (relative), upper left final position of letter Y heading (north), up
     :return: None
    """


    turtle.down()
    turtle.left(90)
    turtle.right(110)
    turtle.left(90)
    turtle.forward(43)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(130)
    turtle.forward(23)
    pass

    turtle.up()

def drawA():
    """
     Draws the letter 'A'
     :pre: pos (relative), lower left initial position of letter A, heading (north),up
     :post: pos (relative), upper left final position of letter A heading (east), up
     :return: None
    """


    turtle.down()
    turtle.right(30)
    turtle.left(120)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    pass

    turtle.up()

def drawK():
    """
     Draws the letter 'K'
     :pre: pos (relative), lower left initial position of letter K, heading (north),up
     :post: pos (relative), upper right final position of letter K heading (north), up
     :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(27)
    turtle.left(180)
    turtle.forward(27)
    turtle.right(90)
    turtle.forward(27)

    pass

    turtle.up()

def drawL():
    """
     Draws the letter 'L'
     :pre: pos (relative), lower left initial position of letter L, heading (north),up
     :post: pos (relative), lower right final position of letter L heading (east), up
     :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    pass

    turtle.up()

def drawI():
    """
     Draws the letter 'I'
     :pre: pos (relative), lower left initial position of letter I, heading (east),up
     :post: pos (relative), upper right final position of letter I heading (west), up
     :return: None
    """

    turtle.down()
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    pass

    turtle.up()


def main():
    """
    The main function which calls all the functions
    :pre: pos (relative), heading (east), up
    :post: pos (relative), heading (east), up
    :return: None
    """
    init(-200)
    drawS()

    init(-170)
    drawH()

    init(-140)
    drawW()

    init(-100)
    drawY()

    init(-80)
    drawA()

    init(-50)
    drawK()

    init(-22)
    drawK()

    init(5)
    drawA()

    init(35)
    drawL()

    init(60)
    drawI()

    input('Hit enter to close...')



    turtle.bye()

if __name__ == '__main__':
    main()