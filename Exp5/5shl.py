import random
import math

BITS, POP_SIZE, GENERATIONS = 10, 20, 5
PC, PM, X_MIN, X_MAX = 0.8, 0.01, 0, 3

def decode(ch):
    num = int(ch, 2)
    return X_MIN + num * (X_MAX - X_MIN) / (2**BITS - 1)

def fitness(ch):
    x = decode(ch)
    return x * math.sin(10 * math.pi * x) + 2

def create_population():
    pop = []
    for i in range(POP_SIZE):
        ch = ""
        for j in range(BITS):
            ch += str(random.randint(0, 1))
        pop.append(ch)
    return pop

def selection(pop, fit):
    total = sum(fit)
    pick = random.uniform(0, total)
    current = 0
    for ch, f in zip(pop, fit):
        current += f
        if current >= pick:
            return ch
    return pop[-1]

def crossover(p1, p2):
    if random.random() < PC:
        point = random.randint(1, BITS - 1)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return c1, c2, point
    return p1, p2, None

def mutation(ch):
    ch = list(ch)
    flipped = []
    for i in range(BITS):
        if random.random() < PM:
            ch[i] = '1' if ch[i] == '0' else '0'
            flipped.append(i + 1)
    return ''.join(ch), flipped

pop = create_population()
best_ch = max(pop, key=fitness)
best_fit = fitness(best_ch)

print("INITIAL POPULATION")
for ch in pop:
    print(ch, "Fitness:", round(fitness(ch), 4))

for gen in range(1, GENERATIONS + 1):
    fit = [fitness(ch) for ch in pop]
    current_best = max(pop, key=fitness)
    current_fit = fitness(current_best)

    if current_fit > best_fit:
        best_ch = current_best
        best_fit = current_fit

    print("\nGENERATION", gen)
    print("Best chromosome:", current_best)
    print("Best x:", round(decode(current_best), 6))
    print("Best fitness:", round(current_fit, 6))

    new_pop = [current_best]
    pair = 1

    while len(new_pop) < POP_SIZE:
        p1 = selection(pop, fit)
        p2 = selection(pop, fit)

        print("\nPair", pair, "- SELECTION")
        print("Parent 1:", p1)
        print("Parent 2:", p2)

        c1, c2, point = crossover(p1, p2)

        print("CROSSOVER")
        if point is None:
            print("No crossover")
        else:
            print("Crossover point:", point)

        print("Child 1 before mutation:", c1)
        print("Child 2 before mutation:", c2)

        c1, flip1 = mutation(c1)
        c2, flip2 = mutation(c2)

        print("MUTATION")
        print("Child 1:", c1, "Flipped bits:", flip1)
        print("Child 2:", c2, "Flipped bits:", flip2)

        new_pop.append(c1)
        if len(new_pop) < POP_SIZE:
            new_pop.append(c2)

        pair += 1

    pop = new_pop

print("\nFINAL RESULT")
print("Best chromosome:", best_ch)
print("Best x:", decode(best_ch))
print("Maximum fitness:", best_fit)