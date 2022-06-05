# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 06:51:42 2022

@author: Amirhossein
"""

import Q5


Objects = list()
Objects_stat = {"Shape": 0, "Circle": 0, "Ellipse": 0, "Rhombus": 0} 

file = open("shapes.txt", "r")
lines = file.readlines()
for line in lines:
    #print("\n"+line+": ")
    name = line.split(' ')

    if name[0] == 'shape':
        a = Q5.Shape()
        Objects.append(a)
        Objects_stat['Shape'] +=1
        a.print()
        
    elif name[0] == 'circle':
        a = Q5.Circle(float(name[1]))
        Objects.append(a)
        Objects_stat['Circle'] +=1
        a.print()
        
    elif name[0] == 'ellipse':
        a = Q5.Ellipse(float(name[1]), float(name[2]))
        Objects.append(a)
        Objects_stat['Ellipse'] +=1
        a.print()
        
    elif name[0] == 'rhombus':
        a = Q5.Rhombus(float(name[1]), float(name[2]))
        Objects.append(a)
        Objects_stat['Rhombus'] +=1
        a.print()
    
    print("\n**************")


file.close()

tottal = 0
for key in Objects_stat.keys():
    tottal += Objects_stat[key]
    print(repr(key) +": "+ repr(Objects_stat[key]))
    
print("Tottal:" + repr(tottal) )
