# find the ascending in the dictionaries:

import operator
#d = { 1:2,2:3,3:4,5:6,4:5,8:12,15:15,1112:14}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print ('orginal dictionari : \n ', d)

sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('dictionaty in ascending order by value : \n', sorted_d)



d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)