import time
import multiprocessing
import tushare as ts


start = time.time()

f=open('E:/6666.txt')
stocks=[line.strip() for line in f.readlines()]
def worker_1():
    d1 = ts.get_realtime_quotes(stocks[0:880])
    print(d1)

def worker_2():
    d2 = ts.get_realtime_quotes(stocks[880:1760])
    print(d2)

def worker_3():
    d3 = ts.get_realtime_quotes(stocks[1760:2640])
    print(d3)

def worker_4():
    d4 = ts.get_realtime_quotes(stocks[2640:3520])
    print(d4)

def worker_5():
    d5 = ts.get_realtime_quotes(stocks[3520:-1])
    print(d5)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = ())
    p2 = multiprocessing.Process(target = worker_2, args = ())
    p3 = multiprocessing.Process(target = worker_3, args = ())
    p4 = multiprocessing.Process(target = worker_4, args = ())
    p5 = multiprocessing.Process(target = worker_5, args = ())


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

end = time.time()
print("\n用时:",end-start)