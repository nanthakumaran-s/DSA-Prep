class Solution:
    # O(n) time | O(n) space
    def hashTable(self, array):
        hashMap = {}
        for num in array:
            if num not in hashMap:
                hashMap[num] = True
            else:
                return num
        return -1

    # O(n) time | O(1) space
    def tortoisemethod(self, array):
        slow = array[0]
        fast = array[0]

        slow = array[slow]
        fast = array[array[fast]]

        while slow != fast:
            slow = array[slow]
            fast = array[array[fast]]

        fast = array[0]

        while slow != fast:
            slow = array[slow]
            fast = array[fast]
        
        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.hashTable([1, 3, 2, 4, 3]))
    print(s.tortoisemethod([1, 3, 2, 4, 3]))
