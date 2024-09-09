import random



sayi="1234567890"
isaret="+-/*!&$#?=@"
harf="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

hane = int(input("şifreniz kaç haneli olsun:"))
sifre = ""
for i in range(hane):
    y =  random.choice(sayi)
    yi=random.choice(isaret)
    yh=random.choice(harf)
    sifre += y  
    sifre+=yi
    sifre+=yh
    print(sifre)
