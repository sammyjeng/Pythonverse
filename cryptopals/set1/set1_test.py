#!/usr/bin/python3
import unittest
from set1 import hex2_base64,fixed_xor,singlebyte_xor,repeating_xor

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

	def test_challenge5(self): 
		key = b"ICE"
		stanza = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
		expected = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
		self.assertEqual(repeating_xor(key,stanza),expected)

challenge1 = Setonetestcase().test_challenge1()

challenge2 = Setonetestcase().test_challenge2()

print(Setonetestcase().test_challenge3())

print(Setonetestcase().test_challenge4())

challenge5 = Setonetestcase().test_challenge5()

if __name__ == '__main__':
	unittest.main()
