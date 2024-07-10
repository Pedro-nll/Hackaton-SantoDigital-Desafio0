def subconjuntos(arr: list, max_size:int, min_size:int, distinct_only:bool, sort_subsets:bool) -> list:
    resposta = [[]]
    
    for i in arr:
        resposta += [subconjuntos_ja_adicionados + [i] for subconjuntos_ja_adicionados in resposta]
        
    if max_size is not None:
        resposta = [subconjunto for subconjunto in resposta if len(subconjunto) <= max_size]
    
    if min_size is not None:
        resposta = [subconjunto for subconjunto in resposta if len(subconjunto) >= min_size]
        
    if distinct_only:
        resposta = [list(set(subconjunto)) for subconjunto in resposta]    
        
    if sort_subsets:
        resposta.sort()
    
    return resposta

print(subconjuntos([1, 2, 2], 2, 1, True, True))