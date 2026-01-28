class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()
        print(clean)
        l,r = 0, len(clean)-1

        while l <= r:
            print(clean[l])
            print(clean[r])
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1 
        return True