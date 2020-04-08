# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-03 14:19:39
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-03 14:31:13
import asyncio

async def phase(i):
    print(f'in phase {i}')
    await asyncio.sleep(5 - (0.1*i))
    print(f'Done phase {i}')
    return f'phase {i} result'

async def main(n):
    print('starting main')
    phases = [
        phase(i)
        for i in range(n)
    ]
    print('waiting for phase to complete')
    result = []
    for nxt in asyncio.as_completed(phases):
        a = await nxt
        print(f'received answer {a}')
        result.append(a)
    print(f'result: {result}')
    return result

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(50))
except:
    event_loop.close()
finally:
    event_loop.close()