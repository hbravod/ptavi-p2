#!/usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import sys

from calcoohija import CalculadoraHija

if len(sys.argv) != 2:
    sys.exit("Úsalo así: python3 calcplusplus.py fichero")

if __name__ == "__main__":

    with open(sys.argv[1], 'r') as csvfile:
        fichero = csv.reader(csvfile)

        calculadora = CalculadoraHija()

        for line in fichero:
            primero = line[0]
            numbers = line[1:]

            if primero == "suma":
                resultado = int(line[1])
                for number in numbers[1:]:
                    resultado = calculadora.suma(resultado, int(number))
                print(resultado)
            elif primero == "resta":
                resultado = int(line[1])
                for number in numbers[1:]:
                    resultado = calculadora.resta(resultado, int(number))
                print(resultado)
            elif primero == "multiplica":
                resultado = int(line[1])
                for number in numbers[1:]:
                    resultado = calculadora.multiplica(resultado, int(number))
                print(resultado)
            elif primero == "divide":
                resultado = int(line[1])
                for number in numbers[1:]:
                    resultado = calculadora.divide(resultado, int(number))
                print(resultado)
