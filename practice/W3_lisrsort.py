#incresin glist by tuples
def last(n): 
	return n[-1]

def sort_list(tuples):
	return sorted(tuples , key=last)

print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

