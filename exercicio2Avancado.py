# RETORNA TRUE SE O PAR JA FOI ADD
def verificar_par(pares_ja_adicionados, novo_par):
    for par in pares_ja_adicionados:
        if (par[0] == novo_par[0] or par[0] == novo_par[1]) and (par[1] == novo_par[0] or par[1] == novo_par[1]):
            return True
    return False

def paresMaisProximos(arr: list, allow_duplicates:bool, sorted_pairs:bool, unique_pairs:bool) -> list:
    if len(arr) < 2:
        raise RuntimeError("ARRAY MUITO PEQUENO")
    
    maior_diff = abs(arr[0] - arr[1])   
    resposta = [(arr[0], arr[1])]
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            par = (arr[i], arr[j])
            
            if not allow_duplicates and arr[i] == arr[j]:
                continue
            
            if unique_pairs and verificar_par(resposta, par):
                continue
            
            if diff == maior_diff:
                resposta.append(par)
            elif diff < maior_diff:
                maior_diff = diff
                resposta = [par]
        
    if sorted_pairs:
        resposta.sort()
        
    return resposta

print(paresMaisProximos([3, 8, 50, 5, 1, 18, 12, 3], False, False, True))