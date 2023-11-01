# Sacar la facturación media de 3 empresas

def fact_prom(empre1 , empre2, empre3):
    total = empre1 + empre2 + empre3
    prom = total / 3
    return prom

Emp1 = int(input('Ingrese la fact de la empresa 1 en USD: ' ))
Emp2 = int(input('Ingrese la fact de la empresa 2 en USD: ' ))
Emp3 = int(input('Ingrese la fact de la empresa 3 en USD: ' ))

resultado = fact_prom(Emp1, Emp2, Emp3)
    
print('La facturación media es de las empresas es de:', resultado)