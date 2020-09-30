import os


path = os.path.join('files', 'dates.txt')
print('The path of the file = ', path)
archivo = open(path, 'r')
data1 = archivo.readline()
data2 = archivo.readline()
data3 = archivo.readline()
data4 = archivo.readline()
data5 = archivo.readline()
data6 = archivo.readline()
data7 = archivo.readline()
data8 = archivo.readline()
archivo.close()

print(data4.split())
