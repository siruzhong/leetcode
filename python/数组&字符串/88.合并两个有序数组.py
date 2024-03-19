class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype
        : None Do not return anything, modify nums1 in-place instead.
        """
        new_num = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                new_num.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                new_num.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                new_num.append(nums1[p1])
                p1 += 1
            else:
                new_num.append(nums2[p2])
                p2 += 1
        nums1[:] = new_num

    # 优化：不使用额外的数组，而是直接在nums1上操作
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype
        : None Do not return anything, modify nums1 in-place instead.
        """
        # 在Python中，切片操作的语法是start:end，其中start是切片开始的索引（包含），end是切片结束的索引（不包含）。
        # nums1[m:]：从nums1的第m个元素开始，截取到最后一个元素。这里的m是包含的。
        # nums2[:n]：从nums2的第0个元素开始，截取到第n-1个元素。这里的n是不包含的。
        nums1[m:] = nums2[:n]
        nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)