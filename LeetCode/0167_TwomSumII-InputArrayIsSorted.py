class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Brute force
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[j] == target - numbers[i]:
                    return [i + 1, j + 1]

    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        # 2 pointers
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum2(numbers, target))
