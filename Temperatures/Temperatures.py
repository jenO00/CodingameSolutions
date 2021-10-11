import sys
import math


# ******************************************** #
# Codingame.com                                #
# Solved: 2021-10-09                           #
# Original problem made by: ?                  #
# Difficulty: Easy                             #
# Solved by: Jennifer00                        #
# *********************************************#

def find_closest(n):
    curr_closest = 0  # current closest numb
    list_temps = []
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)  # cast it to int
        list_temps.append(t)

    for i in list_temps:
        if list_temps.index(i) == 0:  # if it's the first index!
            curr_closest = i
        else:
            if i < 0:  # negative i:s
                pos_i = abs(i)  # a pos version
                if pos_i <= abs(curr_closest):
                    if pos_i == abs(curr_closest):  # If, eg -5 == 5, we choose the pos
                        curr_closest = pos_i
                    else:
                        curr_closest = i
                else:
                    curr_closest = curr_closest  # not smaller
            else:
                if i <= abs(curr_closest):
                    if i == abs(curr_closest):
                        curr_closest = i
                    else:
                        curr_closest = i
                else:
                    curr_closest = curr_closest
    print(curr_closest)


n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)  # if on input
else:
    find_closest(n)
