#! /usr/bin/env python3

import os
from tempfile import mkstemp
from threading import Thread, Lock

MEGA = 2**20
TMP_DIRS = ["/tmp", 
            "/media/ygingras/writable/tmp/", 
            "/media/ygingras/9016-4EF8/tmp"]

def read_rand(size=10*MEGA):
    """ Read size bytes of true random data. """
    return open("/dev/random", "rb").read(size)


def write_many(data, outfile, times=10):
    """ Write data multiple times in outfile. """
    with open(outfile, "ab") as f:
        for i in range(times):
            f.write(data)


def process(tempdir, tempfiles, lock):
    data = read_rand()
    with lock:
        fd, fname = mkstemp(".dat", dir=tempdir)
        tempfiles.append(fname)
    write_many(data, fname)
    print(f"done with {fname}")


def main():
    files = []
    threads = []
    lock = Lock()
    try:
        for i in range(10):
            args = (TMP_DIRS[i%len(TMP_DIRS)], files, lock)
            thread = Thread(target=process, args=args)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    finally:
        # cleanup
        with lock:
            os.system("rm -f %s &" % " ".join(files))

if __name__ == "__main__":
    main()
    
