import random

chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*.,/';:-+()"

length = int(input("Length of password?"))

password = ""

for i in range(length):
    password+=random.choice(chars)

print(password)



