import random
import math
def docFile():
    file = open('input.txt', 'r', encoding='utf-8')
    a = []
    for line in file:
        for so in line.split():
            a.append(int(so.strip()))
    file.close()
    return a
        
def ghiFile():
    file = open('input.txt', 'w', encoding='utf-8')
    for n in range(0, 1000):
        file.writelines(str(random.randint(0, 200)) + "\n")
    file.close()

def soNguyenTo(n):
    snt = 1
    if n < 2:
        return 0
    for s in range(2, round(math.sqrt(n))):
        if n % s == 0:
            snt = 0
            break
    return snt
    
    
snt = 0 
soChan = 0
soLe = 0
arr = docFile()
soLapLai = arr[0]
soLanLap = 1
for n in arr:
    if n % 2 == 0:
        soChan += 1
    else:
        soLe +=1
    if arr.count(n) > soLanLap:
        soLapLai = n
        soLanLap = arr.count(n)
    if soNguyenTo(n) == 1:
        snt += 1
        
print('Co %d so chan' %soChan)
print('Co %d so le' %soLe)
print('Co %d so nguyen to' %snt)
print('So {a} lap lai {al} lan'.format(a = soLapLai , al = soLanLap) )