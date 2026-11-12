import numpy as np

def fitness(x):
    return x * np.sin(10 * np.pi * x) + 2

def find_extrema(pos, fit):
    idx = np.argsort(pos)
    res = ["Neither"] * len(pos)
    for i in range(1, len(pos)-1):
        l, c, r = idx[i-1], idx[i], idx[i+1]
        if fit[c] > fit[l] and fit[c] > fit[r]:
            res[c] = "Local Maximum"
        elif fit[c] < fit[l] and fit[c] < fit[r]:
            res[c] = "Local Minimum"
    return res

def pso(n=10, it=10, low=-1, high=2, w=0.7, c1=1.5, c2=1.5):
    np.random.seed(42)
    pos = np.random.uniform(low, high, n)
    vel = np.random.uniform(-0.1, 0.1, n)
    fit = fitness(pos)
    pbest = pos.copy()
    pfit = fit.copy()
    g = np.argmax(fit)
    gbest = pos[g]
    gfit = fit[g]

    print("Initial Population")
    print("Particle\tPosition\tFitness")
    for i in range(n):
        print(f"{i+1}\t\t{pos[i]:.6f}\t{fit[i]:.6f}")

    vmax = 0.2 * (high-low)

    for t in range(it):
        r1 = np.random.rand(n)
        r2 = np.random.rand(n)
        vel = w*vel + c1*r1*(pbest-pos) + c2*r2*(gbest-pos)
        vel = np.clip(vel, -vmax, vmax)
        pos = np.clip(pos+vel, low, high)
        fit = fitness(pos)

        mask = fit > pfit
        pbest[mask] = pos[mask]
        pfit[mask] = fit[mask]

        g = np.argmax(pfit)
        if pfit[g] > gfit:
            gbest = pbest[g]
            gfit = pfit[g]

        print(f"\nIteration {t+1}")
        print("Particle\tPosition\tFitness")
        for i in range(n):
            print(f"{i+1}\t\t{pos[i]:.6f}\t{fit[i]:.6f}")

        res = find_extrema(pos, fit)
        print("\nLocal Maxima and Minima")
        for i in range(n):
            print(f"Particle {i+1}: x={pos[i]:.6f}, Fitness={fit[i]:.6f}, Result={res[i]}")

        print(f"\nGlobal Best x = {gbest:.8f}")
        print(f"Maximum Fitness = {gfit:.8f}")

    print("\nFinal Results")
    print(f"Optimal x = {gbest:.10f}")
    print(f"Maximum Fitness = {gfit:.10f}")

    return gbest, gfit

best_x, best_fit = pso()