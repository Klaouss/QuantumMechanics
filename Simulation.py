from typing import Any, Union, Tuple

import sympy.physics as sympy
import numpy
import random
import time
import sympy
import scipy.linalg as la
import scipy.constants as sp
from sympy import symbols, Symbol
import math
from numpy import linalg as LA
h = symbols("h")
H = h * symbols("ω")/2
t = symbols("t")
sz = numpy.array([[1,0],[0,-1]])
H = H*sz
i = complex(0.0,1.0)
print("This is a time dependent Quantum Spin Experiment Simulation")
print("Since we don't have a particle, we wil suppose that the Hamiltonian is equal to : hω/2 σz, or :\n",H)
time.sleep(5)
measurement = random.randrange(-1, 2, 2)




aur,aui,adr,adi = random.randint(0,1),random.randint(-1,1),random.randint(0,1),random.randint(0,1)

au,ad = complex(aur,aui),complex(adr,adi)

while au*au.conjugate()+ad*ad.conjugate() !=1:
    aur, aui, adr, adi = round(random.uniform(0.0,1.0),2),round(random.uniform(-1.0,1.0),2),round(random.uniform(0.0,1.0),2),round(random.uniform(-1.0,1.0),2)
    au, ad = complex(aur, aui), complex(adr, adi)
    print(au,ad)
A = [au,ad]
ProbUp = au*au.conjugate()
ProbDown = ad*ad.conjugate()
ProbUp = round(ProbUp.real*100,0)
ProbDown = round(ProbDown.real*100,0)
print("Your Randomly Generated State:",A)
print("If you did the measurement along the z axis: ")
print("Probability of Measurement being 1: ",ProbUp)
print("Probability of Measurement being -1: ",ProbDown)




eigvals = [H[0][0],H[1][1]]
eigvecs = [[1,0],[0,1]]
print("Now knowing that the eigenvalues of the Pauli Matrix for σz, are 1 and -1, and that the eigenvectors are: \n", eigvecs,"\n Using the Hamiltonian, we get that the eigenvalues are: ",eigvals," and the eigenvectors stay the same")

print("We could do the same just by solving the Schrodinger Equation, but there is no need and it is very simple!")
print("However, if you want to do it your self, the time independent schrodinger equation, is nothing else, than the definition of energy eigenvalues and energy eigenvectors, or simply the eigenvectors and eigenvalues of the Hamiltonian!")
time.sleep(0)

print("We already have our initial coefficients and state, but if you didn't, you can calculate them(the initial coefficients, by taking the inner product of each of the energy eigenvector with the initial state")
time.sleep(0)

print("Now we need to capture time dependence, by simply making both initial coefficients and state-vector, functions of time instead of initial")
time.sleep(0)
print("Using unitarity, we get that")

aut = au*sympy.exp((-i*eigvals[0])*t/h)
adt = ad*sympy.exp((-i*eigvals[1])*t/h)


#au,ad = aut,adt
A = [au,ad]
print("Au(t) = ",aut)
print("Ad(t) = ",adt)
print("Time to calculate the final probabilities")


iau = au*i
iad = ad*i
r = au/math.sqrt(2) + ad/math.sqrt(2)
l = au/math.sqrt(2) - ad/math.sqrt(2)
i = au/math.sqrt(2) + iad/math.sqrt(2)
o = au/math.sqrt(2) - iad/math.sqrt(2)

ProbilityUp = (au*au.conjugate()) *100
ProbilityDown =(ad*ad.conjugate())*100
ProbilityRight =( r*r.conjugate())*100
ProbilityLeft =  (l*l.conjugate())*100
ProbilityIn = (i*i.conjugate())*100
ProbilityOut = (o*o.conjugate())*100


print("The Probability, that the spin is in state up, if we measure along the z axis is : ",ProbilityUp)
print("The Probability, that the spin is in state down, if we measure along the z axis is: ",ProbilityDown)
print("The Probability, that the spin is in state right, if we measure along the x axis is : ",ProbilityRight)
print("The Probability, that the spin is in state left, if we measure along the x axis is: ",ProbilityLeft)
print("The Probability, that the spin is in state in, if we measure along the y axis is : ",ProbilityIn)
print("The Probability, that the spin is in state out, if we measure along the y axis is: ",ProbilityOut)



