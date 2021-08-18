class Solution:
    # O(n) time | O(1) space
    def optimal(self, array):
        profit = 0
        mini = float("inf")
        for num in array:
            mini = min(mini, num)
            profit = max(num - mini, profit)
        return profit

if __name__ == "__main__":
    stocks = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.optimal(stocks))