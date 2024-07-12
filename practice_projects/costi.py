import random 

possible_options = [1,2,3,4,5,6]

throw = random.randint(possible_options[0] , possible_options[5])
    
sum = 0 
sum += throw
print(f'Your 1st throw is {sum}')

question = input("Do you need another throw?")

if question == "yes":
    sum += random.randint(possible_options[0] , possible_options[5])
    print(sum)
else:
    print(f"Your sum = {sum}")
    