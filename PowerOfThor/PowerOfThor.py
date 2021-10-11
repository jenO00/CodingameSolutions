import sys
import math


# ******************************************** #
# Codingame.com                                #
# Solved: 2021-09-10                           #
# Original problem made by: ?                  #
# Difficulty: Easy                             #
# Solved by: Jennifer00                        #
# *********************************************#


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if initial_ty > light_y:   #Thor is above light
        if initial_tx == light_x:
            initial_ty -= 1 #Y-coord >
            print("N")
        if initial_tx > light_x:
            initial_tx -= 1 #go west
            initial_ty -=1
            print("NW")
        if initial_tx < light_x:
            initial_tx += 1 #go east
            initial_ty -= 1
            print("NE")
    if initial_ty == light_y: #if same Y-coord
        if initial_tx > light_x:
            initial_tx -= 1
            print("W")  #WEST
        if initial_tx < light_x:
            initial_tx += 1
            print("E") #EAST
    if initial_ty < light_y:
        if initial_tx == light_x: #same X-coord, different Y-coord
            initial_ty += 1
            print("S") #SOUTH
        if initial_tx > light_x:
            initial_tx -= 1
            initial_ty += 1
            print("SW")
        if initial_tx < light_x:
            initial_tx += 1
            initial_ty += 1
            print("SE")


    # A single line providing the move to be made: N NE E SE S SW W or NW