from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == target:
                return (i, j)

# Time complexity: O(n^2)
# Space complexity: O(1)

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}
    for i, num in enumerate(li):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i

# Time complexity: O(n)
# Space complexity: O(n)

def test_find_sum():
    assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
    assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
    print("All tests passed!")

test_find_sum()