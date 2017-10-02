#!/usr/bin/python3

# -*- coding: utf-8 -*-

#import csv
import sys

#from calcoohija import CalculadoraHija

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
        lista=line.split()
        #print(lista)
        primero= line[:line.find(',')]
        print(primero)

         
