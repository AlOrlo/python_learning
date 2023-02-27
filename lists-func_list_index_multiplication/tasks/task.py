from typing import List


def foo(nums: List[int]) -> List[int]:
    result = [1 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            result[i] *= nums[j]
    return result