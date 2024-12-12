import math

filepath = "input.txt"
characters = []
lista = []
listb = []
with open(filepath, 'r') as file:
            for x in file:
                    x = x.split()
                    lista.append(int(x[0]))
                    listb.append(int(x[1]))
print(lista.sort())
print(listb.sort())

distances = []
for i in range(len(lista)):
    distances.append(abs(lista[i]-listb[i]))

print(sum(distances))