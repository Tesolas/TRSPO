from time import sleep
from threading import Thread

def collatz():
    x = input("Enter number: ")
    n = 0
    maxnum = []

    try: 
        x = int(x)
        while x > 1:
            sleep(0.2)
            n += 1
            if x % 2 == 0:
                x /= 2
                print(f'{n}. ({x}) x - odd')
            elif x % 2 != 0:
                x = x*3 + 1
                print (f'{n}. ({x})')
            maxnum.append (x)
        print (f'Max: {max (maxnum)} ')
        print (f'Total: {n}')
    except ValueError:
        print('You entered uncorrect value')


t = Thread(target = collatz)
t.start()
t.join()