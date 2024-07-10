# O(n^2)
def subconjuntos(arr: list) -> list:
    resposta = [[]]
    
    for i in arr:
        resposta += [subconjuntos_ja_adicionados + [i] for subconjuntos_ja_adicionados in resposta]
        
    return resposta

print(subconjuntos([1, 2]))