#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(len(Belgium))

country = "-" * len(Belgium)
print(country)

'''
for i in range(len(Belgium)):
    print("-")
'''

Belgium = Belgium.replace(",", ":")
print(Belgium)

#replace is a method.

population = Belgium.split(":")
print(population)

#argument is passed through the parentheses.

population_Bel = int(population[1])
print(type(population_Bel))

population_Bruss = int(population[3])
print(type(population_Bruss))

sum_Bel_Bruss = population_Bel + population_Bruss
print(sum_Bel_Bruss)




