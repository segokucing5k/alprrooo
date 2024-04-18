len = 12.45
dia = 13.6
pi = 3.14

vol = pi * len * dia * dia / 4

if(vol > 1518.04 and vol < 2099.11):
    print("normal")
elif(vol < 1518.04):
    print("chirrhosis")
elif(vol > 2099.11):
    print("hepatomegaly")


x = 5
y = 10

print("x+y = ", x+y)
print("x-y = ", x-y)
print("x*y = ", x*y)
print("x/y = ", x/y)
print("x**y = ", x**y)
print("x == y = ", x == y)
print("x != y = ", x != y)

num = int(input("Enter a number: "))
factorial = 1
number = 1
while (number <= num):
    factorial *= number
    number += 1
print(factorial)

kalimat = input("Enter a sentence: ")
kal = kalimat.split()

pesan = []

for kata in kal:
    sorted_kata = "".join(sorted(kata))
    pesan.append(sorted_kata)

print(pesan)


data = [120, 131, 125, 140, 130, 119, 128, 115, 127, 150]
for i in data:
    if(130 >= i >= 120):
        print(i, " normal")
    else:
        print(i, " ga Normal")