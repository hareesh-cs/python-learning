import multiprocessing as mp
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds}')

processes=[]
for i in range(10):
    p=mp.Process(target=do_something,args=[1.5])
    p.start()
    processes.append(p)
for process in processes:
    process.join()

finish = time.perf_counter()
print('Finished: %.2f seconds' % (round(finish - start)))
