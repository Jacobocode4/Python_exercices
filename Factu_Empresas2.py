empresas = [7,6,9,11,70,400]

def factu_prom(empresas):
    total = sum(empresas)
    prom = total / len(empresas)
    return prom

resultado = factu_prom(empresas)

print('La facturación media es de: ', resultado)