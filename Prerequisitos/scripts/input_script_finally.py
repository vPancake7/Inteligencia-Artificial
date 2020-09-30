while True:
  try:
    entero = int(input('Ingrese un entero:'))
    break
  except:
  	print('No es un entero, vuelva a ingresarlo')
  finally:
  	print('Se ejecuta si se da un error o no siempre')

print('Convertido en entero ', entero)