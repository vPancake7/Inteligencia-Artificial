print('Haremos una division de numeros donde veremos un error por division cero\n')

(x,y) = (5,0)
try:
    z = x/y
except ZeroDivisionError as e:
    z = e
print(z)
