class Solution:
    def checkPalindrome(self, s:str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return 0
        return 1
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s) - 1):
            for j in range(i, len(s)):
                if self.checkPalindrome(s[i:j]):
                    if len(res) < len(s[i:j]):
                        res = s[i:j]
        return(res)
        
if __name__ == '__main__':
    test_1 = 'kayaka'
    test_2 = 'bb'
    Solution().longestPalindrome(test_1)
    Solution().longestPalindrome(test_2)