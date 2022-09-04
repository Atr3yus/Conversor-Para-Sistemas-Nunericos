bits = int(input("Digite o número de bits: "))
print ("Número maximo a ser convertido: ", -(2**(bits-1)))
valor = int(input("Digite o valor negativo a ser convertido: "))
quociente = abs(valor)
restos = []
while quociente > 0:
    restos.insert(0, quociente % 2)
    quociente = quociente // 2
while len(restos) < bits:
    restos.insert(0,0)
for i in range (len(restos)):
    if restos [i] == 1:
        restos [i] = 0
    else:
        restos [i] = 1
i = len(restos) - 1
restos[i] += 1
while restos [i] > 1:
    restos[i] = 0
    if i >= 0:
        restos[i - 1] += 1
    i -= 1
print("Convertidos para Comp-2: ")
for i in restos:
    print(i, end="")    
        