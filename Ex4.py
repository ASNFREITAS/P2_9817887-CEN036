#!/usr/bin/env python3

print("Cálculo da media das notas.")

Total = 0 #atribuição de valor 0 pra variavel Total
Contador = 0  #atribuição de valor 0 pra variavel Contador
    

while Contador <= 10:            # loop while que fara a somatoria das notas
    num = int(input("Digite uma nota: "))  #pega o imput do usuario para a nota
    Total = num + Total
    Contador = Contador + 1
    
Nota = Total / 10    
print(Nota)

