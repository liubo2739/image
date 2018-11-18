import time
import multiprocessing
import tushare as ts

f=open('E:/6666.txt')
stocks=[line.strip() for line in f.readlines()]
def worker_1():
    for i in stocks[0:880]:
        d1 = ts.get_realtime_quotes(i)
        b = d1['b1_v'].values[0]  # 单个取值方法
        s = d1['a1_v'].values[0]
        name = d1['name'].values[0]
        code = d1['code'].values[0]
        if b != '' and s == '':  # 选出涨停股
            print(code, name,time.ctime())



def worker_2():
    for i in stocks[880:1760]:
        d2 = ts.get_realtime_quotes(i)
        b = d2['b1_v'].values[0]  # 单个取值方法
        s = d2['a1_v'].values[0]
        name = d2['name'].values[0]
        code = d2['code'].values[0]
        if b != '' and s == '':  # 选出涨停股
            print(code, name,time.ctime())



def worker_3():
    for i in stocks[1760:2640]:
        d3 = ts.get_realtime_quotes(i)
        b = d3['b1_v'].values[0]  # 单个取值方法
        s = d3['a1_v'].values[0]
        name = d3['name'].values[0]
        code = d3['code'].values[0]
        if b != '' and s == '':  # 选出涨停股
            print(code, name,time.ctime())




def worker_4():
    for i in stocks[2640:3520]:
        d4 = ts.get_realtime_quotes(i)
        b = d4['b1_v'].values[0]  # 单个取值方法
        s = d4['a1_v'].values[0]
        name = d4['name'].values[0]
        code = d4['code'].values[0]
        if b != '' and s == '':  # 选出涨停股
            print(code, name,time.ctime())




def worker_5():
    for i in stocks[3520:-1]:
        d5 = ts.get_realtime_quotes(i)
        b = d5['b1_v'].values[0]  # 单个取值方法
        s = d5['a1_v'].values[0]
        name = d5['name'].values[0]
        code = d5['code'].values[0]
        if b != '' and s == '':  # 选出涨停股
            print(code, name,time.ctime())


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
