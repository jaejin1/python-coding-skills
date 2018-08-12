from subprocess import Popen, PIPE
import time

proc = Popen(
    ['echo', 'Hello from the chile!!'],
    stdout=PIPE)

out, err = proc.communicate()
print(out.decode('utf-8'))

proc2 = Popen(['sleep', '0.3'])
while proc2.poll() is None:
    print('working...')
    time.sleep(0.1)

print('Exit status ', proc2.poll())

###########################################################################
def run_sleep(period):
    proc = Popen(['sleep', str(period)])
    return proc

start = time.time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()
end = time.time()

print('Finish time %.3f' % (end - start))

###########################################################################
import os

def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Ql13S\x11'
    proc = Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=PIPE,
        stdout=PIPE
    )

    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])

###########################################################################
print('###########################################################################')
def run_md5(input_stdin):
    proc = Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=PIPE
    )
    return proc

input_procs = []
hash_procs = []

for _ in range(3):
    # os.urandom 이라는 함수는 원하는 길이 (byte 단위)의 unsigned 수치값을 만들어준다
    # 'h\xb4\xaa<\x12\xa5\xc8\xaf\xa2sCr\x93 이런거
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())

