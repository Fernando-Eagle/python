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
sobrenome = input("Qual o seu sobrenome?")
idade = input("Qual a sua idade?")
numtest= input("Digite um número para teste:")
import os
if os.name =='nt':
    os.system("cls")
else:
     os.system("clear")
print('-----------------------------------------')
print('Vamos aos Resultados das Entradas')
print('-----------------------------------------')
print("Nome:",nome,sobrenome,"- Idade:",idade)
print("O número de teste digitado era:",numtest)
num = input("Digite um número: ")
print(nome,'o número digitado é:',num)
print ("Como seria se tabalhássemos dois valores?")
num1 = input('Entre com o 1º valor: ')
num2 = input('Entre com o 2º valor: ')
soma = int(num1) + int(num2)
print ("a soma é",soma)
multi = int(num1) * int(num2)
print ("a multiplicação é",multi)
divi = int(num1) / int(num2)
print ("a divisão é",divi)
subtr = int(num1) - int(num2)
print ("a subtração é",subtr)
media = (int(num1) + int(num2))/2
print ("a média é",media)
