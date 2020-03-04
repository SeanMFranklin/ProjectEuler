import csv
from itertools import product


def decrypt(cipher, key):
    res = ""
    for ind, letter in enumerate(cipher):
        res += chr(int(letter) ^ ord(key[ind % 3]))
    return res


keys = [''.join(i) for i in product('abcdefghijklmnopqrstuvwxyz', repeat=3)]
cipher = list(csv.reader(open('p059_cipher.txt')))[0]
words = {i.strip() for i in open('common_words.txt', 'r')}
results = []
for key in keys:
    res = decrypt(cipher, key)
    score = sum(1 for i in words if i in res)
    results.append((score, key))
results.sort(reverse=True)
print(results[:15])
ans = decrypt(cipher, results[0][1])
print(ans, '\n\n', 'Answer:', sum(ord(i) for i in ans))

