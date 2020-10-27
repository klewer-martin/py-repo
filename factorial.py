fact = int(input("Ingrese un numero: "))
res = 1

if fact < 0:
	print('Numero invalido')

else:
	for i in range(fact):
		res += res * i
	print(str(fact) + '! = ' + str(res))
