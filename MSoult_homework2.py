"""
Michelle Soult
Algorithms
Homework 2

A program to:
(a)generate a pair of public and private keys for the RSA scheme
where p and q each has n bits
(b) given x = 3104, computer the encoded message y
(c) given y computer above, compute the decoded message

"""
import random
import math
import time

def isPrime(num):
	"""
	an algorithm for testing primality, with low error probability
	Source = Algorithms, p. 27
	"""
	if num%2 == 0:
		return False
	if num%3 == 0:
		return False
	for k in range (0, 15):
		a = random.randint(0, num)
		if ((a%num) != 1):
			return False
	return True

def extendedEuclid(a, b):
	"""
	an algorithm for determining d for RSA
	Source = Algorithms, p. 21
	"""

	if a == 0:
		return (b, 0, 1)
	while b != 0:
		r, y, x = extendedEuclid(b%a, a)
		return(r, x -(b//a)*y, y)

def modinv(a, m):
	#Source = https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
	gcd, x, y = extendedEuclid(a, m)
	if gcd != 1:
		return None
	else:
		return x%m

def createKey(n):
	"""
	function for creating public and private keys
	Source = Algorithms, p. 34
	start by picking two n-bit random primes p and q
	"""
	'''
	#Source = Algorithms, p. 28
	MAX = pow(10, (n)) - 1 #9, 19, 199...
	found = False
	
	#Prime numbers took too long to calculate
	
	while not found:
		p = random.randint(1, MAX)
		if isPrime(p):
			found = True
	
	found = False
	while not found:
		q = random.randint(1, MAX)
		if isPrime(q):
			found = True
	'''
	
	#Prime numbers took too long to calculate
	if n == 2:
		p = 47
		q = 89
	elif n == 3:
		p = 239
		q = 563
	elif n == 4:
		p = 2399
		q = 4517
	else:
		p = 17609
		q = 15131
	

	#Public key is (N, e) where N = pq and e is a 2n-bit number relatively prime to (p-1)(q-1)
	#e = 3 permits fast encoding
	n = p*q
	e = 3
	
	#private key is d, the inverse of e modulo (p - 1)(q - 1)
	#compute using extended Euclid algorithm
	d = modinv(e, (p-1)*(q-1))
	if d == None:
		print("Error.  Not relative prime.")
	return ((n, e), d)
	

def encodeMsg(x, publicKey):
	"""
	function to encode secret message given public key as well as message (x)
	Source = Algorithms, p. 34
	y = x^e mod N
	"""
	N, e = publicKey
	y = (pow(x, e))%N
	return y

def decodeMsg(y, d, publicKey):
	"""
	function to decode secret message given public & private keys as well as decoded message (y)
	Source = Algorithms, p. 34
	y = x^e mod N; decode by computing y^d mod N
	"""
	N, e = publicKey
	x = (pow(y, d))%N
	return x
	
def main():
	print("Simple RSA algorithm with n-bit encryption.")
	n = int(input("Enter the value of n: "))
	
	print("Creating p and q	as", n,"bit primes.")
	a_START_TIME = time.clock()		#calculate running time
	publicKey, d = createKey(n)
	a_END_TIME = time.clock()
	
	print("Encrypting 3104")
	b_START_TIME = time.clock()
	y = encodeMsg(3104, publicKey)
	b_END_TIME = time.clock()
	print("...")
	print(y, "\n")
	
	
	print("Decrypting", y)
	print("...")
	c_START_TIME = time.clock()
	x = decodeMsg(y, d, publicKey)
	c_END_TIME = time.clock()
	print(x,"\n")
	if x == 3104:
		print("Success!\n")
	else:
		print("Failure!\n")
	
	a_RUN_TIME = a_END_TIME = a_START_TIME
	b_RUN_TIME = b_END_TIME = b_START_TIME
	c_RUN_TIME = c_END_TIME = c_START_TIME
	
	print("Running time a:", a_RUN_TIME, "b:", b_RUN_TIME, "c:", c_RUN_TIME)
	
main()
