# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    for i in arr:
        complement = target - i
        if complement in seen:
            pairs.append((i, complement))
        seen.add(i)
    return pairs
    
arr = [1, 2, 3, 4, 5]
target = 7

print("pairs",pairs_with_sum(arr, target))

