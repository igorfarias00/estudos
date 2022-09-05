# -*- coding: utf-8 -*-
nome = str(input('Digite seu nome: '))
div = nome.split()

print(div[0])

print(nome[(nome.rfind(' '))::])

print(div[len(div) - 1])