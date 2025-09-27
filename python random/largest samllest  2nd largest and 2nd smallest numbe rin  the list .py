a = [1,9,8,7, 6,89,76,54,5,6,34,54,35,67,2,3,4,5,6,7,8,9,]
l1 = max(a)
s1 = min(a)
print(f"the largest value is {l1} and the smallest value is {s1}")
a.remove(s1)
a.remove(l1)

l2= max(a)
s2 = min(a)
print(f"the second largest value is {l2} and the second smallest value is {s2}")