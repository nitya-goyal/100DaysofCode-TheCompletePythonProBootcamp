import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#way 1
rand_index = random.randint(0,4)
print(friends[rand_index])
# way2
print(random.choice(friends))