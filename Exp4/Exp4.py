import random
import math
BITS = 10
POP_SIZE = 20
GENERATIONS = 5
PC = 0.8
PM = 0.01
X_MIN = 0
X_MAX = 1
def decode(chromosome):
    decimal = int(chromosome, 2)
    return X_MIN + decimal * (X_MAX - X_MIN) / (2**BITS - 1)
def fitness(chromosome):
    x = decode(chromosome)
    return x * math.sin(10 * math.pi * x) + 2
def create_population():
    population = []
    for i in range(POP_SIZE):
        chromosome = ""
        for j in range(BITS):
            chromosome += str(random.randint(0, 1))
        population.append(chromosome)
    return population
def roulette_selection(population, fitness_values):
    total = sum(fitness_values)
    pick = random.uniform(0, total)
    current = 0
    for chromosome, fit in zip(population, fitness_values):
        current += fit
        if current >= pick:
            return chromosome
    return population[-1]
def crossover(parent1, parent2):
    if random.random() < PC:
        point = random.randint(1, BITS - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2, point
    return parent1, parent2, None
def mutation(chromosome):
    chromosome = list(chromosome)
    flipped = []
    for i in range(BITS):
        if random.random() < PM:
            chromosome[i] = ('1' if chromosome[i] == '0' else '0')
            flipped.append(i + 1)
    return ''.join(chromosome), flipped
population = create_population()
best_chromosome = max(population, key=fitness)
best_fitness = fitness(best_chromosome)
print("INITIAL POPULATION")
for ch in population:
    print(ch, "Fitness:", round(fitness(ch), 4))
for generation in range(1, GENERATIONS + 1):
    fitness_values = [fitness(ch) for ch in population]
    current_best = max(population, key=fitness)
    current_fitness = fitness(current_best)
    if current_fitness > best_fitness:
        best_chromosome = current_best
        best_fitness = current_fitness
    print("\nGENERATION", generation)
    print("Best chromosome:", current_best)
    print("Best x:", round(decode(current_best), 6))
    print("Best fitness:", round(current_fitness, 6))
    new_population = [current_best]
    pair = 1
    while len(new_population) < POP_SIZE:
        parent1 = roulette_selection(population, fitness_values)
        parent2 = roulette_selection(population, fitness_values)
        print("\nPair", pair, "- SELECTION")
        print("Parent 1:", parent1)
        print("Parent 2:", parent2)
        child1, child2, point = crossover(parent1, parent2)
        print("CROSSOVER")
        if point is None:
            print("No crossover")
        else:
            print("Crossover point:", point)
        print("Child 1 before mutation:", child1)
        print("Child 2 before mutation:", child2)
        child1, flips1 = mutation(child1)
        child2, flips2 = mutation(child2)
        print("MUTATION")
        print("Child 1:", child1, "Flipped bits:", flips1)
        print("Child 2:", child2, "Flipped bits:", flips2)
        new_population.append(child1)
        if len(new_population) < POP_SIZE:
            new_population.append(child2)
        pair += 1
    population = new_population
print("\nFINAL RESULT")
print("Best chromosome:", best_chromosome)
print("Best x:", decode(best_chromosome))
print("Maximum fitness:", best_fitness)