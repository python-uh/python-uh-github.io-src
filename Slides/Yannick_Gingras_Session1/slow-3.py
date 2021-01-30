#! /usr/bin/env python3

import os
from tempfile import mkstemp

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
    print(f"done with {outfile}")


def main():
    files = []
    try:
        for i in range(10):
            data = read_rand()
            fd, fname = mkstemp(f"-{i}.dat", dir=TMP_DIRS[i%len(TMP_DIRS)])
            write_many(data, fname)
            files.append(fname)
    finally:
        # cleanup
        os.system("rm -f %s &" % " ".join(files))

if __name__ == "__main__":
    main()
    
