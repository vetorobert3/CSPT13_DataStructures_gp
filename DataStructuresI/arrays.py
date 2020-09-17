# Linear time iterate over all items
arr = [12, 23, 56, 87, 14]
for num in arr:
    print(num) # O(1)

# constant time lookup
print(arr[3])

# quadratic time nested iteration
for x in arr:  
    for y in arr:
        print(x, y)

# can we do better?

