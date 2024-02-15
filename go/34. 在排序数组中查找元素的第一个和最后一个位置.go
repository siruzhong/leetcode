package main

import "sort"

// 首先找到target出现的第一个位置,然后找到target出现的第二个卫视
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	first := findFirstPosition(nums, target)
	if first == -1 {
		return []int{-1, -1}
	}
	last := findLastPosition(nums, target)
	return []int{first, last}
}

func searchRange2(nums []int, target int) []int {
	l := sort.SearchInts(nums, target)
	if l == len(nums) || nums[l] != target {
		return []int{-1, -1}
	}
	r := sort.SearchInts(nums, target + 1) - 1
	return []int{l, r}
}
// findFirstPosition 找到target出现的第一个位置
func findFirstPosition(nums []int, target int) int {
	l := 0
	r := len(nums) - 1
	for l < r {
		mid := (l + r) / 2
		if nums[mid] < target {
			// 下次搜索的区间为[mid+1,right]
			l = mid + 1
		} else if nums[mid] == target {
			// 下次搜索的区间为[left,mid]
			r = mid
		} else {
			// nums[mid] > target
			// 下次搜索的区间为[left,mid-1]
			r = mid - 1
		}
	}
	if nums[l] == target {
		return l
	}
	return -1
}

// findLastPosition 找到target出现的最后一个位置
func findLastPosition(nums []int, target int) int {
	l := 0
	r := len(nums) - 1
	for l < r {
		mid := (l + r + 1) / 2 // 这里如果有两个分之都是设置left,则mid取值一定要+1(原因可以断点调试进入死循环)
		if nums[mid] < target {
			// 下次搜索的区间为[mid+1,right]
			l = mid + 1
		} else if nums[mid] == target {
			// 下次搜索的区间为[mid,right]
			l = mid
		} else {
			// nums[mid] > target
			// 下次搜索的区间为[left,mid-1]
			r = mid - 1
		}
	}
	// 如果l==r 退出循环
	if nums[l] == target {
		return l
	}
	return -1
}

//func main() {
//	searchRange([]int{5, 7, 7, 8, 8, 10}, 8)
//}
