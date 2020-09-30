while True:
  try:
    entero = int(input('Ingrese un entero:'))
    break
  except:
  	print('No es un entero, vuelva a ingresarlo')

print('Convertido en entero ', entero)