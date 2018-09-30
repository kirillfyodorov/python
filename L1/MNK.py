import random
import matplotlib.pyplot as plt
minX = int(input ('Введите минимальное значение X'))
maxX = int(input ('Введите максимальное значение X'))
minY = int(input ('Введите минимальное значение Y'))
maxY = int(input ('Введите минимальное значение Y'))
x = []
y = []
n=20

def myF(minV, maxV, masV):
	i=0
	while i < n-1:
		log = 0
		t = random.randint(minV, maxV)
		for j in range(len(masV)):
			if t == masV[j]:
				log = 1
				break
		if log == 0:
			masV.append(t)
			i = i + 1
	return (masV)

x = myF(minX, maxX, x)
y = myF(minY, maxY, y)
print ('WOOOOOOW')
print(x)
print ('WOOOOOOW')
print(y)

def sumOne(a):
	i=0
	sumOne = 0
	while i < n-1:
		sumOne = sumOne + a[i]
		i = i + 1
	return (sumOne)

def sumTwo(a, b):
	i=0
	sumTwo = 0
	while i < n-1:
		sumOne = sumOne + a[i]*b[i]
		i = i + 1
	return (sumTwo)

a = (n * sumTwo(x,y) - sumOne(x)*sumOne(y))/(n*sumTwo(x, x)-sumTwo(x, x))
b = (sumOne(y) - a * sumOne(x))/n

fig, _ = plt.subplots()
print(type(fig))



