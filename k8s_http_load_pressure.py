'''
import requests

num_requests = 20

responses = [
    requests.get('http://alexoshttp.alexnamespace01.10.75.58.92.xip.io/')
    for i in range(num_requests)
]
'''
import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://bookinfo.bookinfo.10.75.58.92.xip.io/productpage?u=normal'
        )
        for i in range(20000000)
    ]
    for response in await asyncio.gather(*futures):
        print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())