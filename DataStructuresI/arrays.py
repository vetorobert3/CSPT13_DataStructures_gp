# Linear time iterate over all items
arr = [12, 23, 56, 87, 14]
for num in arr:
    print(num) # O(1)
for num in arr: # Since these are not nested, this is considered a O(1)
    print(num)

# constant time lookup
print(arr[3]) # O(1)

# quadratic time nested iteration
for x in arr: # O(n) 
    for y in arr: # O(n) => O(n^2)
        print(x, y) # O(1) => O(1 * n^2)
# O(n^2) + O(n) + O(1 * n^2)
# O(2n^2) + O(n) => O(n^2) + O(1 * n^2)

# O(n^2)


# can we do better?

