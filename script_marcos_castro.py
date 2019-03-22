#!/usr/bin/python3
#coding: utf-8
import os
if os.name =='nt':
    os.system("cls")
else:
     os.system("clear")

cont = 1
while cont <= 10:
    print('Contador de:', cont)
    cont = cont + 1
print ('Fim do loop')

soma = 0
cont = 1
while cont <=10:
    soma = soma + cont
    cont = cont + 1
print(soma)