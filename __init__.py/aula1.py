# Modulos

import math
#from math import sqrt (é usado para especificar o que será usado da biblioteca)

num = int(input('digite um numero: '))

raiz = math.sqrt(num)

#print('a Raiz de {} e igual a {}' .format(num, raiz))
print('a Raiz de {} e igual a {}' .format(num, math.floor(raiz)))

