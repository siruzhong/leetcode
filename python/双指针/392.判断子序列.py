class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pt1, pt2 = 0, 0
        # 遍历 s 和 t
        while pt1< len(s) and pt2 < len(t):
            # 如果相等，s 往后走一步
            if s[pt1] == t[pt2]:
                pt1 += 1
            # 无论是否相等，t 都要往后走一步
            pt2 += 1
        # 如果 s 遍历完了，说明 s 是 t 的子序列
        return pt1 == len(s)

    
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
    s2 = "axc"
    t2 = "ahbgdc"
    print(Solution().isSubsequence(s2, t2))
    s3 = "aaaaaa"
    t3 = "bbaaaa"
    print(Solution().isSubsequence(s3, t3))
    s4 = "ab"
    t4 = "baab"
    print(Solution().isSubsequence(s4, t4))
