class Solution:
    # O(n) time | O(n) space
    def hashTableMethod(self, array):
        hashTable = {}
        res = []
        for i in range(len(array)):
            num = array[i]
            if num not in hashTable:
                hashTable[num] = True
            else:
                res.append(num)
        for i in range(1, len(array) + 1):
            if i not in hashTable:
                res.append(i)
        return res

    # O(n) time | O(1) space
    def mathematical(self, array):
        length = len(array)
        sum_a = (length * (length + 1)) // 2
        sum_a2 = (length * (length + 1) * (2 * length + 1)) // 6
        for i in range(length):
            sum_a -= array[i]
            sum_a2 -= array[i] ** 2
        missing = (sum_a + sum_a2 // sum_a ) // 2
        repeating = missing - sum_a
        res = [repeating, missing]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.hashTableMethod([1, 3, 4, 2, 6, 6]))
    print(s.mathematical([1, 3, 4, 2, 6, 6]))