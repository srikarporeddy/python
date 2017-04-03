#  we are using count function to find frequency appeared characters i string
#w3_count.py

def char_frequency(str):
	dict = {}
	for n in str:
		keys = dict.keys()
		if n in keys:
			dict[n] += 1
		else:
			dict[n] = 1
	return dict
print(char_frequency(input('enter a string : ')))


string = 'hello worllld : '
dict1 = {}
for char in string:
	dict1[char] = string.count(char)
print(dict1)


'''string = 'hello worllld : '
s = count('string')
print(s)'''