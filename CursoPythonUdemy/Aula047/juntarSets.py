# A coleção set não mantém as duplicatas;
set1 = {"a","b","c"}
set2 = {1,2,3,"b"}

#set1.update(set2)
#print(set1)

#set3 = set1.union(set2)
#print(set1)
#print(set2)
#print(set3)

#set1.intersection_update(set2)
#set3 = set1.intersection(set2) 
#set1.symmetric_difference_update(set2)

set3 = set1.symmetric_difference(set2)
print(set1)
print(set2)
print(set3)
