# Welcome to Sets! Converting list to a set.
lis = [1,1,2,2,3,3,5,5,6,6,7,7,8,8,9,9,10,10]
se = set(lis)

print(lis)
print(se)

# Checking if element is presented in the set.
if 7 in se:
    print("Yes")
else:
    print("No")

# Creating an empty set and adding values to it.
aro = set([])
aro.add(10)
aro.add(4)
aro.add(8)
aro.add(7)
print(aro)

# How to remove the element.
aro.discard(3)

# Set operations.

man = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

# Union
print(man.union(b))
print(man|b)
# Intersection
print(man.intersection(b))
print(man&b)
# Difference
print(man.difference(b))
print(man-b)
# Symmetric Difference
print(man.symmetric_difference(b))
print(man^b)
