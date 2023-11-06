from unittest import result


f = open('DOLECH.INP', 'r')
n = f.readline().split()
data = f.readline()
result = ''
if n[0] == 1 and data[0] == 6:
    D = n <= 3
    D2 = 3 < n <= 6
    result = int(round(D, D2,2))
print(result)
f.close