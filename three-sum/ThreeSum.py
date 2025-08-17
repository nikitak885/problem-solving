def ThreeSum(lst):
    res = []
    n = len(lst)

    # Generating all triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
              
                # If the sum of triplet equals to zero
                # then add it's indexes to the result
                if lst[i] + lst[j] + lst[k] == 0:
                    res.append([lst[i], lst[j], lst[k]])
    return res

listone = [-2,0,2,4,-2,-8]
res = ThreeSum(listone)
print("Triplets output:", res)