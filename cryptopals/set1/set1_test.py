#!/usr/bin/python3
import unittest
from set1 import hex2_base64
from set1 import fixed_xor
from set1 import singlebyte_xor
#from string import ascii_letters as al

class Setonetestcase(unittest.TestCase):

	def test_challenge1(self):
		a = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
		return self.assertEqual(hex2_base64(a), b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

	def test_challenge2(self):
		a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
		b = bytes.fromhex('686974207468652062756c6c277320657965')
		return self.assertEqual(fixed_xor(a,b),b'746865206b696420646f6e277420706c6179')

	def test_challenge3(self):
		a = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
		return (singlebyte_xor(a))

	def test_challenge4(self):
		with open('4.txt','r') as a:
			data = [ bytes.fromhex(x.rstrip('\n')) for x in a]
		for x in data:
			res = singlebyte_xor(x)
			if res != None:
				return (res)

challenge1 = Setonetestcase().test_challenge1()

challenge2 = Setonetestcase().test_challenge2()

print(Setonetestcase().test_challenge3())

print(Setonetestcase().test_challenge4())

if __name__ == '__main__':
	unittest.main()
