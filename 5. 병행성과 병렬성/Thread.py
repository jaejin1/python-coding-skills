import time

def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i

numbers = [1233641, 1258543, 1394223, 3532811]
start = time.time()
for number in numbers:
    list(factorize(number))

end = time.time()
print(end-start)

from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = []
for number in numbers:
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(end-start)

print('###########################################################################')

import select
# 시스템 호출

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print(end-start)


start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    # ...
    assert index < 5

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
print(end-start)