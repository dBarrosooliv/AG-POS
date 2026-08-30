from pyeasyga import pyeasyga
import random

lim_min = -10
lim_max = 10

seed_data = ['x', 'y', 'z']

tamanho_populacao = 100
geracoes = 150

ga = pyeasyga.GeneticAlgorithm(seed_data,
                                population_size=tamanho_populacao,
                                generations=geracoes,
                                crossover_probability=0.9,
                                mutation_probability=0.3,
                                elitism=True,
                                maximise_fitness=False  # queremos MINIMIZAR f
                                )

def my_create_individual(seed_data):
    data = [random.uniform(lim_min, lim_max) for _ in seed_data]
    return data
ga.create_individual = my_create_individual

def aptidao(individual, seed_data):
    x, y, z = individual
    return x**2 + y**2 + z**2
ga.fitness_function = aptidao

def crossover(pai_1, pai_2):
    alpha = random.random()
    filho_1 = [alpha * g1 + (1 - alpha) * g2 for g1, g2 in zip(pai_1, pai_2)]
    filho_2 = [alpha * g2 + (1 - alpha) * g1 for g1, g2 in zip(pai_1, pai_2)]
    return filho_1, filho_2
ga.crossover_function = crossover

def my_mutation(individual):
    indice = random.randrange(len(individual))
    ruido = random.gauss(0, 1)  # desvio padrao 1
    novo_valor = individual[indice] + ruido
    individual[indice] = max(lim_min, min(lim_max, novo_valor))
ga.mutate_function = my_mutation

def my_selection(population):
    torneio = random.sample(population, 3)
    torneio.sort(key=lambda ind: ind.fitness)  # menor fitness primeiro
    return torneio[0]
ga.selection_function = my_selection

ga.run()
melhor_fitness, melhor_individuo = ga.best_individual()
x, y, z = melhor_individuo

print("Melhor individuo encontrado:")
print(f"  x = {x:.6f}")
print(f"  y = {y:.6f}")
print(f"  z = {z:.6f}")
print(f"\nf(x, y, z) = {melhor_fitness:.6f}  (quanto mais perto de 0, mais perto da raiz)")