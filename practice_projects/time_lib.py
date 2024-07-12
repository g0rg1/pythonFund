import time  

RESULT = "Everything is allright"

def pause() -> str:
    seconds = float(input("Введите кол-во секунд которые необходимо ожидать"))
    print(f"Ожидайте {seconds} секунд")
    time.sleep(seconds)
    print(RESULT)
    


    