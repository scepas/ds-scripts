#!/usr/bin/python

#import fileinput
import sys
import re

pattern = re.compile(r'"{2,}')

#(?<!")"{2,}(?!")
def run():
	input_stream = sys.stdin
	for line in input_stream:
		process_line(line)

def process_line(line):
	#replace "" for " ("id"" -> "id")
	l = pattern.sub('"', line)
	print l,
	#print line

if __name__ == "__main__":
	try:
		run()
	except ValueError, e:
		print >> sys.stderr, e
		sys.exit(1)
