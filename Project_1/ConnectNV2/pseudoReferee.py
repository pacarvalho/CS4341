#!/usr/bin/env python
import sys

sys.stdout.write("6 7 3 1 1\n")
sys.stdout.flush()

while 1:
	if len(sys.stdin.readline().split()) is not 0:
		sys.stdout.write("1 1\n")
		sys.stdout.flush()