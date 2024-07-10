# O(n^2)
def paresMaisProximos(arr: list) -> list:
    if len(arr) < 2:
        raise RuntimeError("ARRAY MUITO PEQUENO")
    
    maior_diff = abs(arr[0] - arr[1])   
    resposta = [(arr[0], arr[1])]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff == maior_diff:
                resposta.append((arr[i], arr[j]))
            elif diff < maior_diff:
                maior_diff = diff
                resposta = [(arr[i], arr[j])]
        
    return resposta

print(paresMaisProximos([3, 8, 50, 5, 1, 18, 12]))