import numpy as np

def calculate(list):
    # Verifica se a lista contém exatamente 9 elementos
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em um array NumPy 3x3
    arr = np.array(list).reshape(3, 3)

    # Cria o dicionário de cálculos com as operações 
    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()],
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()],
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()],
        'max': [np.amax(arr, axis=0).tolist(), np.amax(arr, axis=1).tolist(), np.amax(arr).tolist()],
        'min': [np.amin(arr, axis=0).tolist(), np.amin(arr, axis=1).tolist(), np.amin(arr).tolist()],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
    }

    return calculations

# Testando a função com o exemplo dado
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
