valor = input("Digite o valor positivo a ser convertido: ")
base = int(input("digite a base para qual se deseja converter: "))
expoente = 0
decimal = 0
for i in range (len(valor)-1, -1, -1):
    decimal += int (valor[i])* (base**expoente)
    expoente += 1
print("({}) {} = ({}) 10".format(valor, base, decimal))