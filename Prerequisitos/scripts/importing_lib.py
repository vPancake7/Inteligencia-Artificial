# importando todas las funciones
import lib.functions
print(lib.functions.mult(3,2))

# importar la libreria con alias
import lib.functions as lf
print(lf.suma(3,2))

#importando funciones especificas
from lib.functions import div, resta 
print(div(1,2))
print(resta(4,2))

# importar funciones especificas con alias
from lib.functions import suma as s, resta as r
print(s(1,1))
print(r(1,1))

from lib.functions import * # importar todo 
print(lib.functions.div(1,3))

