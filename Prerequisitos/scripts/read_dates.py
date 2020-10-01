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

record4 = data4.split()
fecha = record4[2]
fecha1 = record4[3]
fecha2 = record4[4]
print(fecha, fecha1, fecha2)

record4 = data5.split()
fecha = record4[2]
fecha1 = record4[3]
fecha2 = record4[4]
print(fecha, fecha1, fecha2)

record4 = data6.split()
fecha = record4[2]
fecha1 = record4[3]
fecha2 = record4[4]
print(fecha, fecha1, fecha2)


record4 = data7.split()
fecha = record4[2]
fecha1 = record4[3]
fecha2 = record4[4]
print(fecha, fecha1, fecha2)

record4 = data8.split()
fecha = record4[2]
fecha1 = record4[3]
fecha2 = record4[4]
print(fecha, fecha1, fecha2)


