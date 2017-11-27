"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Damon Kintner.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

import rosegraphics as rg

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################


window = rg.TurtleWindow()

blueTurtle = rg.SimpleTurtle('turtle')
blueTurtle.pen = rg.Pen('blue',3)
blueTurtle.speed = 10

redTurtle = rg.SimpleTurtle('turtle')
redTurtle.pen = rg.Pen('red',3)
redTurtle.speed = 5

size = 250

for k in range (5):

    blueTurtle.draw_square(size)
    redTurtle.draw_circle(size)

    blueTurtle.right(90)
    blueTurtle.forward(15)
    redTurtle.left(90)
    redTurtle.forward(15)

    size = size - 25

window.close_on_mouse_click()

