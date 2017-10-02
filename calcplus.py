#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija

if len(sys.argv) != 2:
    sys.exit("Úsalo así: python3 calcplus.py fichero")

if __name__ == "__main__":

    fichero = open(sys.argv[1], 'r')
    texto = fichero.readlines()

    calculadora = CalculadoraHija()

    for line in texto:
        lista = line.split(',')
        primero = lista[0]
        numbers = lista[1:]

        if primero == "suma":
            resultado = int(lista[1])
            for number in numbers[1:]:
                resultado = calculadora.suma(resultado, int(number))
            print(resultado)
        elif primero == "resta":
            resultado = int(lista[1])
            for number in numbers[1:]:
                resultado = calculadora.resta(resultado, int(number))
            print(resultado)
        elif primero == "multiplica":
            resultado = int(lista[1])
            for number in numbers[1:]:
                resultado = calculadora.multiplica(resultado, int(number))
            print(resultado)
        elif primero == "divide":
            resultado = int(lista[1])
            for number in numbers[1:]:
                resultado = calculadora.divide(resultado, int(number))
            print(resultado)
fichero.close
