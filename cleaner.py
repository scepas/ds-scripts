#!/usr/bin/env python

#import fileinput
import sys
import re

pattern = re.compile(r'"{2,}')
pattern_date = re.compile(r'"(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d)-\d\d:\d\d"')

#(?<!")"{2,}(?!")
def run():
	input_stream = sys.stdin
	for line in input_stream:
		process_line(line)

def process_line(line):
	#replace "" for " ("id"" -> "id")
	l = pattern.sub('"', line)
	#TODO: convert dates to hive compliant timestamps: 2013-05-10T23:59:59-08:00 -> 2013-05-10 23:59:59
	l = pattern_date.sub(r'\1 \2', line)
	#print line
	print l,
	

if __name__ == "__main__":
	try:
		run()
	except ValueError, e:
		print >> sys.stderr, e
		sys.exit(1)
