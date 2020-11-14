import numpy as np
import scipy as sp
from scipy.optimize import linprog
print("------------------------INPUT----------------")
print()
maximize = input('Do you want to maximize objective function? ').lower()
if(maximize[0]=='y'):
    maximize = 1
else:
    maximize = -1
variables = int(input('Number of variables: '))
c = [0]*variables

print("Give Objective Function: ")
for i in range(variables):
    coeff = input('Write coefficient of x'+str(i+1)+' variable : ')
    c[i] = maximize*int(coeff)

bounds = [(0,None)]*variables
number_of_inequalities = int(input('Number of inequalities : '))
A = []
print("Give equation of bounds")
for i in range(number_of_inequalities):
    l = [0]*variables
    print("Give equation of bounds of equation",i+1)
    for j in range(variables):
        coeff = input('Write coefficient of x'+str(j+1)+' variable : ')
        l[j] = coeff
    A.append(l)
b = []
for i in range(number_of_inequalities):
    b_val = int(input("Input upper bound of each equation "+str(i+1)+"= "))
    b.append(b_val)
print()
print("------------------------OUTPUT----------------")
print()
res = linprog(c, A_ub=A, b_ub=b,  bounds=tuple(bounds), 
              method='revised simplex', options={"disp": True})

print(res)
