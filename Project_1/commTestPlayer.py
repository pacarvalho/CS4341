#!/usr/bin/env python

import sys
import io

# Tests the communication to the referee

sys.stdout.write("The Name\n")
sys.stdout.flush()

stream = sys.stdin
reader = io.open(stream.fileno(), mode='rb', closefd=False)

sys.stdout.write("3 1\n")
sys.stdout.flush()

while 1:
	sys.stdout.write(str(reader.readline()))
	sys.stdout.flush()
