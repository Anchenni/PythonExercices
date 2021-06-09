import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#a = random.sample(range(100), 16)
#b = random.sample(range(100), 20)

#intersection_set = set.intersection(set(a), set(b))
#intersection_list = list(intersection_set)



#print(list(set.intersection(set(a),set(b))))

print(list(set.intersection(set(random.sample(range(100), 16)),set(random.sample(range(100), 20)))))

