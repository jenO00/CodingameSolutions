import sys
import math

# ******************************************** #
# Codingame.com                                #
# Solved: 2021-10-11                           #
# Original problem made by: AminGholizad       #
# Difficulty: Easy                             #
# Solved by: Jennifer00                        #
# *********************************************#

n = int(input())


def validate(card):
    new_card = []
    int_card = []
    single_digit_sum = 0
    odd_digit_sum = 0
    for i in card:
        if i != " ":  # get rid of all spaces
            int_card.append(int(i))
    int_card.reverse()  # reverse the list! so we can go through it from right to left
    index = 0  # index counter
    single_digs = []
    odd = []
    for i in int_card:
        if index % 2 != 0:  # index 0, 3, 5... not divisible by 2
            if i * 2 >= 10:
                single_digit_sum = int(str(i * 2)[0]) + int(str(i * 2)[1])
                new_card.append(single_digit_sum)
                single_digs.append(single_digit_sum)
                single_digit_sum = 0  # make it zero again
            else:
                new_card.append(i * 2)  # digits * 2 is never odd. 2*k % 2 == 0
                single_digs.append(i * 2)
        if index % 2 == 0 or index == 0:
            odd_digit_sum += i
            odd.append(i)
            new_card.append(i)
        index += 1
    final_sum = 0
    for i in single_digs:
        final_sum += i
    result = final_sum + odd_digit_sum
    if result % 10 != 0:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    for i in range(n):
        card = input()
        validate(card)  # call validate for every single test
