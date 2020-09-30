import os


path = os.path.join('files', 'bookstore.txt')
print('The path of the file = ', path)
archivo = open(path, 'r')
data = archivo.read()
archivo.close()

print(data)
