import time
import asyncio
import requests


async def myfun():
    await asyncio.sleep(3)
    print("func 1 3 seconds")

async def myfun2():
    await asyncio.sleep(1)
    print("func 1 second")
    
async def myfun3():
    await asyncio.sleep(4)
    print("func 1 4 seconds")
    
async def main():
    task = asyncio.create_task(myfun())
    await myfun()
    await myfun2()
    await myfun3()

asyncio.run(main())

# incomplete see video boring....................