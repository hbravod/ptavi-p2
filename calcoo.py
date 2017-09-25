#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def __init__(self,operando1,operando2):
        """Esto es el método iniciliazador"""
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        return self.operando1+self.operando2

    def resta(self):
        return self.operando1-self.operando2

    if len(sys.argv) != 4:
        sys.exit("Úsalo así: pyhton3 calcoo.py operando1 operador operando2")


    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters. Only 'int' parameters.")

if __name__ == "__main__":

    operacion = Calculadora(int(sys.argv[1]), int(sys.argv[3]))

    if sys.argv[2] == "suma":
        resultado = operacion.suma()
    elif sys.argv[2] == "resta":
        resultado = operacion.resta()
    else:
        sys.exit('Operación sólo puede ser suma o resta.')

    print(resultado)
