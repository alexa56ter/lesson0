grages=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Stive','Khendrik','Aaron'}
students1=sorted(list(students))
grages[0]= float(5+3+3+5+4)/5
grages[1]= float(2+2+2+3) /4
grages[2]= float (4+5+5+2)/4
grages[3]= float (4+4+3)/3
grages[4]= float (5+5+5+4+5)/5
otwet= dict(zip(students1, grages))
print(otwet)
print(type(otwet))
#print(dict)