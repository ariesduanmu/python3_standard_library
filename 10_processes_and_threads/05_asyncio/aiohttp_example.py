# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-03 15:29:13
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-03 15:31:34
async def gather_tasks():
    async with aiohttp.ClientSession() as session:
        coroutines = (fetch(session, URI.format(stock))
                        for stock in STOCKS)
        return await asyncio.gather(*coroutines)

async def fetch_end_render():
    for i, response in enumerate(await gather_tasks()):
        _render_response(i, response)