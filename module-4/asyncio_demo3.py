import asyncio


async def func1():
    task = asyncio.create_task(func2())
    # return_val=await task
    # print(return_val)

    print('A')
    await asyncio.sleep(2)
    # await func2()
    print('B')
    return_val=await task
    print(return_val)


async def func2():
    print('1')
    await asyncio.sleep(3)
    print('2')
    return 10

asyncio.run(func1())