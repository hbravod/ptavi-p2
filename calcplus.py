#!/usr/bin/python3

# -*- coding: utf-8 -*-

#import csv
import sys

from calcoohija import CalculadoraHija

if len(sys.argv) != 2:
    sys.exit("Úsalo así: python3 calcplus.py fichero")
        

if __name__ == "__main__":

#    with open('calcplus.txt', newline= '') as csvfile:
#        texto = csv.reader(csvfile, delimiter=' ', quotechar='|')
#        for row in texto:
#            print(', '.join(row))

    fichero=open('/home/alumnos/hbravod/ptavi/ptavi-p2/operaciones','r')
    num=fichero.readlines()

    
    for line in num:
        lista=line.split(',')
        primero=lista[0]

        if primero == "suma":
            resultado1 = int(lista[1])+int(lista[2])+int(lista[3])+int(lista[4])+int(lista[5])
            print(resultado1)
        elif primero == "resta":
            resultado2 = int(lista[1])-int(lista[2])-int(lista[3])-int(lista[4])-int(lista[5])
            print(resultado2)
        elif primero == "multiplica":
            resultado3 = int(lista[1])*int(lista[2])*int(lista[3])
            print(resultado3)   
        elif primero == "divide":
            resultado4 = int(lista[1])/int(lista[2])/int(lista[3])
            print(resultado4)



















fichero.close      
