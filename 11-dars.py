a = int(input("Son kiriting"))
n = list(range(1, a + 1))
s = sum(n)
print(f"{' '.join(map(str, n))} Sum : {s}")


#2-masala

a = int(input("1-Son kiriting"))
n = int(input("2-Son kiriting"))
p = 1
for i in range(1, n + 1):
    print(i, end=" ")
    p *= i
print(f"The Multiply is : {p}")

a = int(input("Son kiriting"))
for i in range (2, a, 2):
    print(i)

a = int(input("Son kiriting"))
for i in range (1, a, 2 ):
    print(i)

a = int(input("Son kiriting"))
for i in range(a, 0, -1):
    if i % 2 == 0:
        print(i, " ")



a = int(input("Son kiriting"))
for i in range(a, 0, -1):
    if i % 2 == 1:
        print(i, " ")

a = int(input("Son kiriting"))
for i in str(a):
    print(i, " ")

b = int(input("Son kiriting"))
for i in range(b, 0, -1):
    if i % 2 == 0:
        print(i, " ")

a = int(input("Son kiriting"))
for i in range(a, 0, -1):
    if i % 2 == 1:
        print(i, " ")



for number in range(100, 200):
    s = str(number)
    if s.count(s[0]) == 2 or s.count(s[1]) == 2 or s.count(s[2]) == 2:
        print(number, " ")

a = int(input("Son kiriting"))
for i in range(a, 0, -1):
    if i % 2 == 1:
        print(i, " ")





n = int(input("uchburchakning balandligini kiriting:"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i) 