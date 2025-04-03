#Created by user snoyes
import sys
import math

def check_words(mayhem_report):
    curr_caps_word = ""
    isDone = False
    hasStarted = False
    for letter in mayhem_report: 
        if letter.isupper() and isDone == False and mayhem_report.index(letter) != 0:
            curr_caps_word += letter
            hasStarted = True
        elif letter == " " and isDone == False and hasStarted == True:
            curr_caps_word += letter
        elif mayhem_report.index(letter) == len(mayhem_report)+1:
            hasStarted = False
            isDone = True
        else:
           pass
    return curr_caps_word

cyborg_count = int(input())
if cyborg_count == 1: 
    print(input())
else:
    cyborgs = []
    cyborg_dict = {}
    for i in range(cyborg_count):
        cyborg_name = input()
        cyborgs.append(cyborg_name)
        cyborg_dict[cyborg_name] = []
    mayhem_report_count = int(input())
    mayhem = []

    for i in range(mayhem_report_count):
        mayhem_report = input()
        curr_word = check_words(mayhem_report)
        mayhem.append(curr_word)


    cyborg_report_count = int(input())

    for i in range(cyborg_report_count):
        cyborg_report = input()
        for name in cyborgs:
            cyborg_rep = []
            if name in cyborg_report: 
                name_index = len(name)+2
                curr_rep = check_words(cyborg_report[name_index:])
                cyborg_dict[name].append(curr_rep)


    curr_leader = ""
    curr_max = 0
    cyborg_points = {}
    for name in cyborg_dict: 
        cyborg_points[name] = 0
        curr_count = 0
        for value in cyborg_dict[name]:
            if value in mayhem: 
                cyborg_points[name] += 1
            else:
                cyborg_points[name] -= 1 #no match


    if all(value < 0 for value in cyborg_points.values()):
        print("INDETERMINATE")
    else:
        max_points = max(cyborg_points.values())
        max_count = sum(1 for value in cyborg_points.values() if value == max_points)
        if max_count > 1: 
            print("MISSING")
        else: 
            print(max(cyborg_points, key=cyborg_points.get))  
