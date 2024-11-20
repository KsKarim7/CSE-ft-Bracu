import random


def two_point_crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)  
    point2 = random.randint(point1 + 1, len(parent1) - 1) 

    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return offspring1, offspring2, point1, point2


parent1 = "000111000"
parent2 = "111000111"



offspring1,offspring2, point1, point2  = two_point_crossover(parent1, parent2)


print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Crossover Points:", point1, "and", point2)
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)
