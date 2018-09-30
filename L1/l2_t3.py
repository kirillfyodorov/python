# -*- coding: utf-8 -*-
import random
from math import log
n = 20
matO = []
disp = []
logmas = []
matOLog = []

def createArray():
	return [[random.randint(0,30) for i in range(n)] for j in range(n)]


def matem(mas):
	for i in range(n):
		matO.append(0)
		disp.append(0)
		for j in range(n):
			matO[i] = matO[i]+mas[i][j]
		matO[i]=round(float(matO[i])/n, 3)
		for j in range(n):
			disp[i] = (mas[i][j] - matO[i])**2 + disp[i]
		disp[i] = round(disp[i]/n, 3)

def matemlog(mas):
	for i in range(n):
		matOLog.append(0)
		for j in range(n):
			matO[i] = matO[i]+mas[i][j]
		matO[i]=round(float(matO[i])/n, 3)

def linKor(m,k,mas,matO):
	r = 0
	deli = 0
	for i in range(n):
		r = r + (mas[m][i] - matO[m])*(mas[k][i] - matO[k])
		deli = deli + ((mas[m][i] - matO[m])**2)*((mas[k][i] - matO[k])**2)
		if deli == 0:
			deli = 0.00000000000000000001
		r = round((r**2)**0.5/deli**0.5, 3)
	return(r)


def logor(mas):
	for i in range(n):
		strk = []
		logmas.append(strk)
		for j in range(n):
			if mas[i][j]==0:
				logmas[i].append(-30)
			else: 
				logmas[i].append(log(mas[i][j]))




mas = createArray()
print('Заполненный массив: ', mas)
print
matem(mas)
logor(mas)
matemlog(logmas)
print('Матрица мат.ожиданий: ', matO)
print('Матрица дисперсий: ', disp)

p = input('Вверите допустимую погрешность для проверки порреляции\n')
print('Линейно коррелируют ряды:')
x=0
while x<n-1:
	y = x+1
	while y<n:
		if (1-p)<=linKor(x,y,mas,matO):
			print(x, y)
		y=y+1
	x=x+1

print('Экспоненциально коррелируют ряды:')
x=0
y=0
while x<n:
	while y<n:
		if x==y:
			y=y+1
			continue
		elif (1-p)<=linKor(x,y,logmas,matOLog):
			print(x, y)
		y=y+1
	x=x+1
	y=0
