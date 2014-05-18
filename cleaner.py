#!/usr/bin/python

#import fileinput
import sys

#def clean_line:

def run():
	input_stream = sys.stdin
	for line in input_stream:
		process_line(line)

def process_line(line):
	print line
	print "eeeeeh"


if __name__ == "__main__":
	try:
		run()
	except ValueError, e:
		print >> sys.stderr, e
		sys.exit(1)
