"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

nums = [int(i) for i in open("Euler13.txt", "rb")]
print(str(sum(nums))[:10])
