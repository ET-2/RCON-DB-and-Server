import aiohttp
import asyncio
import json

from tenacity import retry, stop_after_attempt


@retry(stop=stop_after_attempt(5))
async def call_rcon(url, params):
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, params=params, verify_ssl=False) as resp:
                data = await resp.json()
                data_result = data.get('result')

                if resp.status == 200 and data_result:
                    print(f'[{resp.status}] {resp.url}')
                    return data_result

                elif resp.status != 200:
                    print(f'Response Status: {resp.status}')
    except:
        raise Exception


if __name__=="__main__":
    asyncio.run(start())
