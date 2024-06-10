import asyncio
from typing import List
import importlib

wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        index = 0
        while index < len(results) and results[index] < delay:
            index += 1
        results.insert(index, delay)
    return results
