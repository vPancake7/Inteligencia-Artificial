
def suma(a, b):
	return a+b

a = 4

def main():
  print('probando enteros')
  assert(suma(3,2) == 5)

  print('probando flotantes')
  assert(suma(1.2, 2.3) == 3.5)
  print('paso las pruebas')
  
if __name__ == '__main__':
  print('from my file to import')
  print(suma(3,2))
  main()
