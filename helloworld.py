#!/usr/bin/env python
"""
Sleepy Hello World
"""

import sys
from time import sleep

sleep(180)  # wait for 180 seconds

sys.stdout.write("\n\n\nHello, World!\n\n\n")

with open('python_output.txt','w') as my_output:
    my_output.write("Hello, World!")

