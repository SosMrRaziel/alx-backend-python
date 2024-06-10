#!/usr/bin/env python3
""" The basics of async """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    completed_tasks = []
    for task in asyncio.as_completed(tasks):
        completed_task = await task
        completed_tasks.append(completed_task)
    return sorted(completed_tasks)
