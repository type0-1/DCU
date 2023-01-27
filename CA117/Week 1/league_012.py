#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
layout = ["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]
old = 0
for team in inputs:
   team = team.split()
   name = ""
   for i in range(len(team)):
      if team[i].lower().isalpha() or team[i] == "&":
         name += team[i] + " "
   curr = len(name)
   if old < curr:
      old = curr
titleCheck = True
for i in range(2):
    if titleCheck:
        pos = layout[0]
        club = f'{layout[1]:<{old}}'
        fField = ""
        otherFields = ""
        for i in range(2, len(layout)):
            if i == 2:
               fField = f'{layout[i]:>1}'
            else:
               otherFields += f'{layout[i]:>{4}}'
        twoTitles = pos + " " + f'{club:<{old}}'
        print(twoTitles, fField + otherFields)
        titleCheck = False
    else:
        for team in inputs:
           team = team.split()
           string = ""
           name = ""
           string = f'{team[0]:>{len(layout[0])}}'
           for i in range(len(team)):
              if team[i].lower().isalpha() or team[i] == "&":
                 name += team[i] + " "
           name = f'{name:<{old}}'
           number_list = []
           for i in range(1, len(team)):
              if int(team[i].isdigit()) or team[i][0] == "-":
                 number_list.append(team[i])
           fPoints = ""
           restofPoints = ""
           for i in range(len(number_list)):
              if i == 0:
                 fPoints += f'{number_list[i]:>2}'
              else:
                 restofPoints += f'{number_list[i]:>4s}'
           result = name + fPoints + restofPoints
           print(string, result)