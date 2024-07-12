import random

a =int(input("Введите начало"))
b = int(input("Введите конец"))

c = random.randint(a , b)
print(c)

d = int(input("Введите свое число"))
i = 0

while c != d:
    i +=1
    print(f"Try number:{i}")
    d = int(input("Введите свое число"))
    
if c == d :
    print(f"You win in {i+1} tries")
    

