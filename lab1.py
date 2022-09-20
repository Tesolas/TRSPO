from time import sleep, perf_counter
from threading import Thread


def do1():
    sleep(3)

def do2():
    sleep(2)

def do3():
    sleep(5)

start_time = perf_counter()

t1 = Thread(target = do1)
t2 = Thread(target = do2)
t3 = Thread(target = do3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = perf_counter()

print(f'it took {end_time - start_time: 0.2f} seconnds to complete')
