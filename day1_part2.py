import math

filepath = "input.txt"
lista = []
listb = []
sim_score = {}
with open(filepath, 'r') as file:
            for x in file:
                    x = x.split()
                    lista.append(int(x[0]))
                    listb.append(int(x[1]))
                    a = int(x[0])
                    b = int(x[1])
                    if b not in sim_score:
                            sim_score[b] = 1
                    else:
                            sim_score[b] = sim_score[b] + 1
#print(lista.sort())
#print(listb.sort())
distances = 0
for i in lista:
    if i not in sim_score:
        w = 0
    else:
        w = sim_score[i]
    distances = distances + (i * w)

print(distances)