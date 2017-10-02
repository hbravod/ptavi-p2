#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def suma(self, operando1, operando2):
        return operando1 + operando2

    def resta(self, operando1, operando2):
        return operando1 - operando2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Úsalo así: pyhton3 calcoo.py operando1 operador operando2")
    operacion = Calculadora(int(sys.argv[1]), int(sys.argv[3]))
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters. Only 'int' parameters.")

    if sys.argv[2] == "suma":
        resultado = operacion.suma()
    elif sys.argv[2] == "resta":
        resultado = operacion.resta()
    else:
        sys.exit('Operación sólo puede ser suma o resta.')

    print(resultado)
