def summary(x , y: int) -> int:
    print (x + y )

def minus(x , y:int) -> int:
    print (x - y )

def multip (x,y:int) ->int:
    print( x * y)

def delit(x , y :int) ->int:
    print( x / y)

while True:

    print("Choose operation 1.+ ; 2.- ; 3.* , 4./")
    operation = int(input("Choose:"))

    num_1 = int(input("Num 1 =?"))
    num_2 = int(input("Num 2 =?"))

    if operation == 1:
        summary(num_1,num_2)
        break
    elif operation == 2:
        minus(num_1 , num_2)
        break
    elif operation == 3:
        multip(num_1 , num_2)
        break
    elif operation == 4:
        delit(num_1 ,num_2)
        break
    else:
        print("INCORRECT OPERRATION")
        continue
