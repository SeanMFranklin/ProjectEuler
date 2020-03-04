"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
big = 0
bigi = 0
bigj = 0

def rev(l):
	r = ""
	for k in str(l):
		r = k+r
	return r



for i in range(100, 1000):
	for j in range(100, 1000):
		if str(i*j) == rev(i*j) and i*j > big:
			big = i*j
			bigi = i
			bigj = j
print(big)
print(bigi)
print(bigj)

