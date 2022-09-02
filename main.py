valor = int(input("Digite o valor no Sistema Decimal: "))
base = int(input("digite a base para qual se deseja converter: "))
quociente = abs(valor)
restos = ""
while quociente > 0:
  restos += str(quociente % base)
  quociente = quociente // base
if (valor > 0):
  print("({})10 = ({}) {}".format(valor, restos[::-1],base))
else:
  print("({})10 = (-{}) {}".format(valor, restos[::-1],base))
