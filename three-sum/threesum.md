Given an array of integers nums, return the Triplets nums[i], nums[j] and nums[k], where  nums[i] + nums[j] + nums[k] == 0 and the indices i,j and k are all distinct.

You may return the output and the triplets in any order.

Return the answer with the smaller index first.

Example 1:
```
Input:
    nums = [-2,0,2,4,-2,-8]

Output: 
    [[-2, 0, 2], [-2, 4, -2], [0, 2, -2]]

```

```

Explanation:
nums[0] + nums[1] + nums[2] = (-2) + 0 + 2 = 0.
nums[1] + nums[2] + nums[4] = 0 + 2 + (-2) = 0.
nums[0] + nums[3] + nums[4] = (-2) + 4 + (-2) = 0.
The distinct triplets are [-2,0,2] , [-2,-2,4] and [0, 2, -2].

```

Example 2:
```
Input: 
    nums = [0, -1, 2, -3, 1]

Output: 
    [[0, -1, 1], [2, -3, 1]]
```
Example 3:
```
Input: 
    nums = [-1, -1, 0, -5, 5, 6, 1]

Output: 
    [[-1, 0, 1], [-1, -5, 6], [-1, 0, 1], [-1, -5, 6], [0, -5, 5]]
```