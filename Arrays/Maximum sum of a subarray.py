class Solution:
    # O(n^3) time | O(1) space
    def n3Sol(self, array):
        maxi = float("-inf")
        for i in range(len(array)):
            for j in range(i, len(array)):
                sumOfNum = 0
                for k in range(i, j):
                    sumOfNum += array[k]
                maxi = max(sumOfNum, maxi)
        return maxi

    # O(n^2) time | O(1) space
    def n2Sol(self, array):
        maxi = float("-inf")
        for i in range(len(array)):
            sumOfNum = 0
            for j in range(i, len(array)):
                sumOfNum += array[j]
                maxi = max(sumOfNum, maxi)
        return maxi

    # O(n) time | O(1) space
    def kadane(self, array):
        sumOfNum = 0
        maxi = float("-inf")
        for num in array:
            sumOfNum += num
            maxi = max(sumOfNum, maxi)
            sumOfNum = sumOfNum if sumOfNum > 0 else 0
        return maxi

if __name__ == "__main__":
    s = Solution()
    arr = [-2, -3, 4, -1, -2, 1, 5, -4]
    print(s.n3Sol(arr))
    print(s.n2Sol(arr))
    print(s.kadane(arr))
