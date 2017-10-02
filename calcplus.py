#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija

if len(sys.argv) != 2:
    sys.exit("Úsalo así: python3 calcplus.py fichero")

if __name__ == "__main__":

    fichero = open('/home/alumnos/hbravod/ptavi/ptavi-p2/operaciones', 'r')
    num = fichero.readlines()

    for line in num:
        lista = line.split(',')
        primero = lista[0]

        if primero == "suma":
            resultado = int(lista[1])+int(lista[2])+int(lista[3])+int(lista[4])
            resultado1 = resultado+int(lista[5])
            print(resultado1)
        elif primero == "resta":
            resultado2 = int(lista[1])-int(lista[2])
            re = resultado2-int(lista[3])
            res = re-int(lista[4])
            resu = res-int(lista[5])
            resultado3 = resu-int(lista[6])
            print(resultado3)
        elif primero == "multiplica":
            resultado4 = int(lista[1])*int(lista[2])*int(lista[3])
            print(resultado4)
        elif primero == "divide":
            resultado5 = int(lista[1])/int(lista[2])/int(lista[3])
            print(resultado5)
fichero.close
