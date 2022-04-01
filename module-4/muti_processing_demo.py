import multiprocessing as mp
import time

start = time.perf_counter()


def do_something():
    print("Sleeping for 1 second ")
    time.sleep(1)
    print('Done sleeping')


p1 = mp.Process(target=do_something)
p2 = mp.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()
finish = time.perf_counter()
print('Finished: %.2f seconds' % (round(finish - start)))
