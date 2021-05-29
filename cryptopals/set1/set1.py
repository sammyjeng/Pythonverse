#!/usr/bin/python3
from string import ascii_letters as al,punctuation
import binascii
from base64 import b64encode


def hex2_base64(a):
	hd = binascii.unhexlify(a)
	return b64encode(hd)

def fixed_xor(a,b):
	if len(a) == len(b):
		return binascii.hexlify(bytes([ a1 ^ b1 for a1,b1 in zip(a,b)]))

def singlebyte_xor(a):
	temp = []
	total = {}
	freq = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u'];
	dep = 0
	cnt = 0
	for ch in range(1,255):
		temp = [ str(chr((ch) ^ (i))) for i in a]
		for i in temp:
			if i in freq:
				cnt += 5
			elif i in al:
				cnt += 3
			elif i in punctuation:
				cnt -= 5
		dep = cnt
		cnt = 0
		temp = ''.join(temp)
		if dep > 100:
			total[dep] = temp
			return total
		else:
			continue

if '__name__' == '__main__':
	main()
