package main

import (
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	// 第一层循环
	for i := 0; i < len(nums); i++ {
		// 需要和上一次枚举的数不相同
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		// 第三重循环的指针初始指向数组的最右端
		k := len(nums) - 1
		// 第二层循环
		for j := i + 1; j < len(nums); j++ {
			// 需要和上一次枚举的数不相同
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}
			// 保证第二层循环指针j在第三层循环指针k的左侧
			for j < k && nums[i]+nums[j]+nums[k] > 0 {
				k--
			}
			// 如果指针重合，随着后续j的增加，不会存在 i+j+k=0 且 j<k 的情况，可以退出循环
			if j == k {
				break
			}
			if judge(nums[i], nums[j], nums[k]) {
				res = append(res, []int{nums[i], nums[j], nums[k]})
			}
		}
	}
	return res
}

func judge(a, b, c int) bool {
	if a+b+c == 0 {
		return true
	}
	return false
}
