def topKFrequent(nums, k):
    res = []
    counts = [[] for _ in range(len(nums)+1)]
    freq = {}

    for num in nums:
        freq[num] = 1 if num not in freq else freq[num]+1
    for key, val in freq.items():
        counts[val].append(key)

    for count in counts[::-1]:
        if count:
            for num in count:
                res.append(num)
        if len(res) == k:
            break

    return res

print(topKFrequent([7,7], 1)) #[7]