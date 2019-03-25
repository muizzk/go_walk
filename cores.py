from multiprocessing import Process

def worker(num):
    print("Worker:", num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
