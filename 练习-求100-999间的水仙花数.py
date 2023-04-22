#计算100-999间的水仙花数(一个三位数的每一位的三次方之和等于这个数)
suma=0
print('100到999之间的水仙花数有：')
for a in range(100,1000):
    for b in str(a):
        suma+=int(b)**3
    if suma==a:
        print(suma)
    suma=0

