#!/usr/bin/python3
#coding: utf-8
import os
if os.name =='nt':
    os.system("cls")
else:
     os.system("clear")

print('Hello, World')
print('Este é um pequeno programa em Python')
print('Estamos executando em Python3')
print('-----------------------------------------')
nome = input("Qual o seu nome?")
x=5
print(nome,"havia uma variável que era 'x' e valia:",x)
num = int(input("Digite um número: "))
y = num
print(nome,'o número digitado é:',  y)
print ("Como seria se tabalhássemos dois valores?")
num1 = int(input('Entre com o 1º valor: '))
num2 = int(input('Entre com o 2º valor: '))
soma = num1 + num2
print ("a soma é",soma)
multi = int(num1) * int(num2)
print ("a multiplicação é",multi)
divi = int(num1) / int(num2)
print ("a divisão é",divi)
subtr = int(num1) - int(num2)
print ("a subtração é",subtr)
media = (int(num1) + int(num2))/2
print ("a média é",media)
