# 스레드에서 데이터 경쟁을 막으려면 Lock을 사용하자
from threading import Thread
from threading import Lock

class Counter(object):
    def __init__(self):
        self.count = 0
    def increment(self, offset):
        self.count += offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # 센서에서 읽어옴
        counter.increment(1)

def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args) # args 는 무조건 튜플이어야 한다
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

how_many = 10**5
counter = Counter()
run_threads(worker, how_many, counter)
print('counter should be %d, found %d' %
      (5 * how_many, counter.count))

class LockingCounter(object):
	def __init__(self):
		self.lock = Lock()
		self.count = 0

	def increment(self, offset):
		with self.lock:
			self.count += offset

counter = LockingCounter()
run_threads(worker, how_many, counter)
print('counter should be %d, found %d' %
      (5 * how_many, counter.count))