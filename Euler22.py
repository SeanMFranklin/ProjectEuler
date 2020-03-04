totalsum=0

text = (open("Euler22.txt", "r"))				#Opens the file as text
lines = text.read().split(',')					#Pulls all the names into a list
lines = ([s.replace('"', '') for s in lines])	#Removes the "

print(lines.sort())								#Sorts the list
print(lines)

print(lines[1])									#Prints the first name
print(lines[1][0])								#Prints the first letter
print(ord(lines[1][0]))							#Prints the ascii value of first letter

k=0
for i in lines:									#Loops over the names in the list
	k+=1										#Represents position in the list
	wordsum = 0									#Initializes the sum per word
	for j in i:									#Loops over each letter in the name
		wordsum += ord(j) -64					#Adds the word value to the sum where A = 1, B = 2, ...
	totalsum += wordsum*k						
print(totalsum)

