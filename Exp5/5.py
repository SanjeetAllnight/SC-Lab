import random
import math
POP_SIZE = 20
CHROMOSOME_LENGTH = 10
GENERATIONS = 5
MUTATION_RATE = 0.01

def fitness(x):
    return x * math.sin(10 * math.pi * x) + 2

def decode(chromosome):
    decimal = int(chromosome, 2)
    return decimal / (2**CHROMOSOME_LENGTH - 1)

def selection(population):
    fitness_values = [fitness(decode(c)) for c in population]
    total = sum(fitness_values)
    pick = random.uniform(0, total)

    current = 0
    for chromosome, value in zip(population, fitness_values):
        current += value
        if current >= pick:
            return chromosome

    return population[-1]
#Single-Point Crossover. Selects a random position and exchanges the remaining bits of two parents to create two children.
def crossover(p1, p2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    return (p1[:point] + p2[point:],
            p2[:point] + p1[point:]), point
#Bit-Flip Mutation.1% chance of 0to1 or 1 to 0 
def mutate(chromosome):
    bits = list(chromosome)
    flipped = []
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            bits[i] = '1' if bits[i] == '0' else '0'
            flipped.append(i)
    return ''.join(bits), flipped

population = [
    ''.join(random.choice('01') for _ in range(CHROMOSOME_LENGTH))
    for _ in range(POP_SIZE)
]
#repeats algo 5 times:sort,elitism,selection,crossover,mutation,replacement,summary.
for generation in range(GENERATIONS):
    print(f"GENERATION {generation + 1}")

    population.sort(key=lambda c: fitness(decode(c)), reverse=True)

    print("\n[Step 1] Current population (sorted by fitness):")
    print(f"{'No.':<4} {'Chromosome':<12} {'x':<10} {'Fitness':<10}")
    for i, c in enumerate(population, 1):
        print(f"{i:<4} {c:<12} {decode(c):<10.4f} {fitness(decode(c)):<10.4f}")

    new_population = [population[0]]
    print(f"\n[Step 2] Elitism: best chromosome {population[0]} "
          f"(fitness {fitness(decode(population[0])):.4f}) carried over")

    print("\n[Step 3] Creating offspring:")
    pair_no = 1
    while len(new_population) < POP_SIZE:
        p1 = selection(population)
        p2 = selection(population)

        (c1, c2), point = crossover(p1, p2)
        m1, flips1 = mutate(c1)
        m2, flips2 = mutate(c2)

        print(f"\n  Pair {pair_no}:")
        print(f"    Parent 1 : {p1}  (x={decode(p1):.4f}, f={fitness(decode(p1)):.4f})")
        print(f"    Parent 2 : {p2}  (x={decode(p2):.4f}, f={fitness(decode(p2)):.4f})")
        print(f"    Crossover point: {point}")
        print(f"    After crossover : {c1}  {c2}")
        print(f"    After mutation  : {m1}  {m2}")
        print(f"    Bits flipped    : child1={flips1 if flips1 else 'none'}, "
              f"child2={flips2 if flips2 else 'none'}")

        new_population.append(m1)
        if len(new_population) < POP_SIZE:
            new_population.append(m2)
        pair_no += 1

    population = new_population

    best_gen = max(population, key=lambda c: fitness(decode(c)))
    avg_fit = sum(fitness(decode(c)) for c in population) / POP_SIZE
    print(f"\n[Step 4] Generation {generation + 1} summary:")
    print(f"    Best chromosome : {best_gen}")
    print(f"    Best x          : {decode(best_gen):.4f}")
    print(f"    Best fitness    : {fitness(decode(best_gen)):.4f}")
    print(f"    Average fitness : {avg_fit:.4f}\n")

best = max(population, key=lambda c: fitness(decode(c)))
x = decode(best)


print("FINAL RESULT")
print("Best Chromosome:", best)
print("Best x:", x)
print("Maximum Fitness:", fitness(x))
