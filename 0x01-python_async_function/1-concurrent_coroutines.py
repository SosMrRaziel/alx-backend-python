#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random
import importlib


wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """ Waits for a random delay between 0 and max_delay """
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    resaults = []
    for completed in asyncio.as_completed(tasks):
        result = await completed
        resaults.append(result)



    return resaults
