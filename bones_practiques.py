#!/usr/bin/env python

'''Bones pràctiques. Hem de calcular la divisió entera de dos nombres i
indicar el resultat

Institut Icària
Programació - 1r Batxillerat - Curs 2024-25

Utilitzant el dividend i divisor, dos nombres que tu escolliras,
el programa calculara el quocient, el residu i els ensenya a la pantalla.
Seguidament ensenya el procés de la divisió.
programa i el resultat esperat.
'''

__author__ = "Iker Aragonés Peláez"
__email__ = "iaragones@instituticaria.cat"
__date__ = "2024/10/23"

dividend = int(input("introdueix el dividend: "))
divisor = int(input("introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
