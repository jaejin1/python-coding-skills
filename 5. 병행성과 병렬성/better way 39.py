# 스레드 간의 작업을 조율하려면 Queue를 사용하자
from threading import Lock
from collections import deque
from threading import Thread
import time

class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    #@property
    def get(self):
        with self.lock:
            return self.items.popleft()

    #@lock.setter
    def put(self, item):
        with self.lock:
            self.items.append(item)

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1
def download():
    print('download')
def resize():
    print('resize')
def upload():
    print('upload')

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

#while len(done_queue.items) < 1000:# 스레드 간의 작업을 조율하려면 Queue를 사용하자
from threading import Lock
from collections import deque
from threading import Thread
import time

class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    #@property
    def get(self):
        with self.lock:
            return self.items.popleft()

    #@lock.setter
    def put(self, item):
        with self.lock:
            self.items.append(item)

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1
def download():
    print('download')
def resize():
    print('resize')
def upload():
    print('upload')

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

#while len(done_queue.items) < 1000:
    # 기다리는 동안 작업

processed = len(done_queue.items)

polled = sum(t.polled_count for t in threads)
print(processed, polled)


    # 기다리는 동안 작업

processed = len(done_queue.items)

polled = sum(t.polled_count for t in threads)
print(processed, polled)

