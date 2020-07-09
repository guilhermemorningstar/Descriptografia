from contextlib import suppress
from string import ascii_lowercase


resultado = []
alfabeto = list(ascii_lowercase)

# Ignora o erro
# 

codigo = str(input('digite o codigo: '))
key = int(input('Tente adivinhar a chave: '))
x = 3
y = 0
guardar = 0
resultadoFinal = []

with suppress(Exception):
    for trio in codigo:
        guardar = codigo[y:x]
        guardar = int(guardar)
        y += 3
        x += 3
        resultado.append(chr(guardar))

resultado = resultado[::-1]

for allP in range(len(resultado)):
    for allA in range(len(alfabeto)):
        if(alfabeto[allA] == resultado[allP]):
            allA = allA-key
            print(f'{alfabeto[allA]}', end='')
