import os


path = os.path.join("files", "bookstore.txt")
print('The path of the file = ', path)
titles = [line.rstrip() for line in open(path)]
archivo = open(path, 'r')
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
data = archivo.readline()
archivo.close()

print(data)
