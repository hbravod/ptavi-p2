#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora


class CalculadoraHija(Calculadora):
    def multiplica(self):
        return self.operando1 * self.operando2

    def divide(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed.")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Úsalo así: pyhton3 calcoohija.py operand1 operador operand2")
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters. Only 'int' parameters.")

    operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))

    if sys.argv[2] == "suma":
        resultado = operacion.suma()

    elif sys.argv[2] == "resta":
        resultado = operacion.resta()

    elif sys.argv[2] == "multiplica":
        resultado = operacion.multiplica()

    elif sys.argv[2] == "divide":
        resultado = operacion.divide()

    print(resultado)
