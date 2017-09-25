#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija():

    def __init__(self, operando3, operando4):
        self.operando3 = operando3
        self.operando4 = operando4

    def multiplica(self):
        return self.operando3 * self.operando4
    
    def divide(self):
        return self.operando3 / self.operando4

    if len(sys.argv) != 4:
        sys.exit("Úsalo así: pyhton3 calcoohija.py operando1 operador operando2")
    try:
        operando3 = int(sys.argv[1])
        operando4 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters. Only 'int' parameters.")

if __name__ == "__main__":

    operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))

    if sys.argv[2] == "multiplica":
        resultado = operacion.multiplica()

    elif sys.argv[2] == "divide":
        try:
            resultado = operacion.divide()
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed.")

    print(resultado)
