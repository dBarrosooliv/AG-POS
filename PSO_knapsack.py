import pyswarms as ps
import numpy as np
 
data = [{'cor': 'verde',   'valor': 4,  'peso': 12},
        {'cor': 'cinza',   'valor': 2,  'peso': 1},
        {'cor': 'amarelo', 'valor': 10, 'peso': 4},
        {'cor': 'laranja', 'valor': 1,  'peso': 1},
        {'cor': 'azul',    'valor': 2,  'peso': 2}]
 
CAPACIDADE = 15
QTD_MAX = 15 
 
def aptidao(enxame, data):
    resultados = []
    for particula in enxame:
        quantidades = np.clip(np.round(particula), 0, QTD_MAX).astype(int)
        peso = sum(qtd * caixa['peso'] for qtd, caixa in zip(quantidades, data))
 
        if peso > CAPACIDADE:
            fator = CAPACIDADE / peso
            quantidades = np.floor(quantidades * fator).astype(int)
 
        dinheiro = sum(qtd * caixa['valor'] for qtd, caixa in zip(quantidades, data))
        resultados.append(dinheiro)
    return -np.array(resultados)  # pyswarms minimiza -> negativo pra maximizar
 
options = {'c1': 1.5, 'c2': 1.5, 'w': 0.7}
limites = (np.zeros(len(data)), np.ones(len(data)) * QTD_MAX)
 
pso = ps.single.GlobalBestPSO(n_particles=30,
                               dimensions=len(data),
                               options=options,
                               bounds=limites)
 
melhor_custo, melhor_posicao = pso.optimize(aptidao, iters=100, data=data)
 
quantidades = np.clip(np.round(melhor_posicao), 0, QTD_MAX).astype(int)
peso_total = sum(qtd * caixa['peso'] for qtd, caixa in zip(quantidades, data))
if peso_total > CAPACIDADE:
    fator = CAPACIDADE / peso_total
    quantidades = np.floor(quantidades * fator).astype(int)
    peso_total = sum(qtd * caixa['peso'] for qtd, caixa in zip(quantidades, data))
 
print("\nQuantidades:", quantidades)
print("Dinheiro:", sum(qtd * caixa['valor'] for qtd, caixa in zip(quantidades, data)))
print("Peso total:", peso_total)