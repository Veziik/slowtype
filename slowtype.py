#! /usr/bin/env python3
import sys
import time

symbols = ".?!\'-:;[]{}()\"\\—1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\t "
out = ''
print('')
delay = 0

for i in range(0,len(sys.argv)):
	if sys.argv[i] == '-t':
		delay = float(sys.argv[i+1])



with open(sys.argv[1], 'r' ) as file:
	text = file.read()

	for i in range(0, len(text)):
		if text[i] == '\n':
			print('')
			sys.stdout.flush()
			out = ''
		else:
			for symbol in symbols:
				sys.stdout.write('\r%s' % out + symbol)
				sys.stdout.flush()
				time.sleep(delay)
				if symbol == text[i]:
					out += symbol
					break
			

				

print('\n')