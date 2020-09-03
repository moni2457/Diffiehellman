import random

p = input("Please input p:")
g = input("Please input g:")

a = random.randint(1, 10)
b = random.randint(1, 10)
print ("Random secret number at Sa")
print ("Random secret number at Sb")

A = ((pow(g, a)) % p)
B = ((pow(g, b)) % p)
print ("Ta = ", str(A))
print ("Tb = ", str(B))

Ka = ((pow(B, a)) % p)
Kb = ((pow(A, b)) % p)
print ("Secret key at A = ", str(Ka))
print ("Secret key at B = ", str(Kb))