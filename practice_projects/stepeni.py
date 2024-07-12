import random 

possible = ['Love' , 'No Love']

list = [ ]

i = 0 

while i < 50:
    list.append(random.choice(possible))
    i+=1
    
print(random.choice(list))