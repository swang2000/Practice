def findMaximumXOR(nums):
    answer = 0
    for i in range(32)[::-1]:
        answer <<= 1
        prefixes = {num >> i for num in nums}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer


nums = [3, 10, 5, 25, 2, 8]
findMaximumXOR(nums)
