from queue import Queue
from threading import Thread
import time
queue = Queue(1)

def consumer():
    time.sleep(0.1)
    print('test')
    queue.get()
    print('consumer got 1')
    queue.get()
    print('consumer got 2')

thread = Thread(target=consumer())
thread.start()

queue.put(object())
print('producer put 1')
queue.put(object())
print('producer put 2')
thread.join()
print('producer done')

