import math
"""Area del Circulo"""
def area_circulo(radio):

  return math.pi * radio **2
print(area_circulo(5))

"""Area rectangulo"""
def area_rectangulo(ancho, alto):
  return ancho*alto
print(area_rectangulo(4, 6))

"""Area Triangulo"""
def area_triangulo(base, altura):
  return (base*altura)/2
print(area_triangulo(3, 8))

"""Factorial"""
def factorial(numero):
  if numero == 0 or numero == 1:
    return 1
  else:
    resultado = 1
    for i in range(2, numero + 1):
      resultado *=i
    return resultado
print(factorial(5))    


"""Es Primo"""
def es_primo(numero):
  if numero < 2:
    return False
  for i in range(2, int(numero**0.5)+1):
    if numero % i == 0:
      return False
    return True
print(es_primo(7))
print(es_primo(10)) 

"""Area Poligono Regular"""
def area_poligono_regular(n_lados, longitud_lado):
  if n_lados < 3:
    return "Un poligono debe tener al menos 3 lados"
  return (n_lados * longitud_lado **2) / (4 * math.tan(math.pi / n_lados))
print(area_poligono_regular(6, 4))
