#! /usr/bin/env python3

import os
import asyncio
import concurrent
from tempfile import mkstemp
import aiofiles

MEGA = 2**20
TMP_DIRS = ["/tmp", 
            "/media/ygingras/writable/tmp/", 
            "/media/ygingras/9016-4EF8/tmp"]


def read_rand(size=10*MEGA):
    """ Read size bytes of true random data. """
    return open("/dev/random", "rb").read(size)


async def write_many(data, outfile, times=10):
    """ Write data multiple times in outfile. """
    async with aiofiles.open(outfile, "ab") as f:
        for i in range(times):
            await f.write(data)

async def process(fname):
    data = read_rand()
    await write_many(data, fname)
    print(f"done with {fname}")

async def main():
    files = []
    tasks = []
    loop = asyncio.get_running_loop()
    try:
        for i in range(10):
            fd, fname = mkstemp(f"-{i}.dat", dir=TMP_DIRS[i%len(TMP_DIRS)])
            files.append(fname)
            
            task = await asyncio.to_thread(process, fname)
            tasks.append(task)
            
        await asyncio.gather(*tasks)

    finally:
        # cleanup
        print("star up cleanup")
        os.system("rm -f %s &" % " ".join(files))
        os.system("sleep 30 &")
        print("done with cleanup")

if __name__ == "__main__":
    asyncio.run(main())
    
