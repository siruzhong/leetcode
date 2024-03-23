class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().replace(" ", "")
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        if s == s[::-1]:
            return True
        return False

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().replace(" ", "")
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        pt1, pt2 = 0, len(s) - 1
        while pt1 < pt2:
            if s[pt1] != s[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        return True
    

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
    print(Solution().isPalindrome2(s))
    s2 = "race a car"
    print(Solution().isPalindrome(s2))
    print(Solution().isPalindrome2(s2))
    s3 = " "
    print(Solution().isPalindrome(s3))
    print(Solution().isPalindrome2(s3))