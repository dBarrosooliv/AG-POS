from pyeasyga import pyeasyga
import random

#Dados (pesoxvalor)
data = [{'name': 'green', 'value': 4, 'weight': 12},
        {'name': 'gray', 'value': 2, 'weight': 1},
        {'name': 'yellow', 'value': 10, 'weight': 4},
        {'name': 'orange', 'value': 1, 'weight': 1},
        {'name': 'blue', 'value': 2, 'weight': 2}]

CAPACIDADE = 15
QTD_MAX = CAPACIDADE

tamanho_populacao = 100
geracoes = 200

ga = pyeasyga.GeneticAlgorithm(data,
                                population_size=tamanho_populacao,
                                generations=geracoes,
                                crossover_probability=0.9,
                                mutation_probability=0.3,
                                elitism=True,
                                maximise_fitness=True
                                )


#::: Individuo: um gene por item, indicando a quantidade escolhida daquele item
def my_create_individual(data):
    data_individuo = [random.randint(0,15), random.randint(0,15),random.randint(0,15),random.randint(0,15),random.randint(0,15)]
    return data_individuo


ga.create_individual = my_create_individual
 
def aptidao(individual, data):
    peso_total = 0
    valor_total = 0
    for i in range(len(data)):
        peso_total += individual[i] * data[i]['weight']
        valor_total += individual[i] * data[i]['value']
 
    if peso_total > CAPACIDADE:
        return -1
 
    return valor_total
ga.fitness_function = aptidao
 
def crossover(fonte1, fonte2):
    i = random.randrange(1, len(fonte1))
    filho_1 = fonte1[:i] + fonte2[i:]
    filho_2 = fonte2[:i] + fonte1[i:]
    return filho_1, filho_2
ga.crossover_function = crossover
 
def my_mutation(individual):
    mutacao_i = random.randrange(len(individual))
    individual[mutacao_i] = random.randint(0, QTD_MAX)
ga.mutate_function = my_mutation
 
def my_selection(population):
    # ::: Torneio: pega 3 individuos aleatorios e devolve o melhor deles
    torneio = random.sample(population, 3)
    torneio.sort(key=lambda ind: ind.fitness, reverse=True)
    return torneio[0]
ga.selection_function = my_selection
 
ga.run()

fitness, melhor_individuo = ga.best_individual()

print("Melhor individuo:", melhor_individuo)

peso_total = 0
valor_total = 0
print("\nItens:")
for i in range(len(data)):
    qtd = melhor_individuo[i]
    if qtd > 0:
        cor = data[i]['name']
        peso_item = qtd * data[i]['weight']
        valor_item = qtd * data[i]['value']
        peso_total += peso_item
        valor_total += valor_item
        print(f"  {cor:8s} x{qtd:2d}  (peso {peso_item:3d}, valor {valor_item:3d})")

print(f"\nPeso total : {peso_total} kg (limite: {CAPACIDADE} kg)")
print(f"Valor total: ${valor_total}")
