#w3_listcount.py
# find first and last  values in string are same

def match_words(words):
	ctr = 0

	for word in words:
		if len(word) > 1 and word[0]==word[-1]:
		 	ctr += 1
	return ctr
print (match_words(['abba' , '1221' , 'tomoto']))

