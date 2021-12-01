class Solution:
    # O(log(n)) time | O(1) space
    def power(self, x, n):
        result = 1.0
        isChanged = False
        if n < 0: 
            n *= -1
            isChanged = True
        while n:
            if n % 2:
                result *= x
                n -= 1
            else:
                x = x * x
                n = n // 2
        if isChanged:
            result = 1 / result
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.power(2, -1))