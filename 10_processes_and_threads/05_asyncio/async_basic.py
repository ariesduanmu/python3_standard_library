# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-03 15:17:50
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-07 16:36:21
import asyncio

async def two1():
    print('starting two1')
    await asyncio.sleep(2)
    print('hey two1')
    return 2

async def two2():
    print('starting two2')
    await asyncio.sleep(2)
    print('hey two2')
    return 2

async def four():
    print('starting four')
    await asyncio.sleep(4)
    print('hey four')
    return 4

async def main():
    await two1()
    await two2()
    await four()
    # print(await asyncio.gather(two1(), two2(), four()))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
except:
    event_loop.close()
finally:
    event_loop.close()
