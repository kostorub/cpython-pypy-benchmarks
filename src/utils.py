import functools
import time
from collections import defaultdict
from typing import Any, Callable, ParamSpec

P = ParamSpec("P")

average_time_map: dict[str, list[float]] = defaultdict(list)


def timeitit(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        average_time_map[func.__name__].append(run_time)
        return value

    return wrapper_func
