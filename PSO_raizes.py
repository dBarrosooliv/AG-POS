import pyswarms as ps
import numpy as np

lim_min = -10
lim_max = 10
dim = 3  # x, y, z

def aptidao(enxame):
    # enxame: shape (n_particulas, 3) -> cada linha e uma posicao (x, y, z)
    x = enxame[:, 0]
    y = enxame[:, 1]
    z = enxame[:, 2]
    return x**2 + y**2 + z**2


options = {'c1': 1.5, 'c2': 1.5, 'w': 0.7}

limites = (np.array([lim_min] * dim),
           np.array([lim_max] * dim))

pso = ps.single.GlobalBestPSO(n_particles=40,
                               dimensions=dim,
                               options=options,
                               bounds=limites)

melhor_custo, melhor_posicao = pso.optimize(aptidao, iters=100)

x, y, z = melhor_posicao

print("\nMelhor posicao encontrada:")
print(f"  x = {x:.6f}")
print(f"  y = {y:.6f}")
print(f"  z = {z:.6f}")
print(f"\nf(x, y, z) = {melhor_custo:.6f}")