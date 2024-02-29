# time_get_clock_info.py

import textwrap
import time

available_clock = [
        ('clock', time.clock),
        ('monotonic', time.monotonic),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
        ('time', time.time),
]

for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
    {name}:
        adjustable:
