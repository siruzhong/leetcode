package main

// 将数组一分为二，其中一定有一个是有序的，另一个可能有序，也能是部分有序。
// 此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	l := 0
	r := len(nums) - 1
	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[l] <= nums[mid] { // 左边有序
			if nums[l] <= target && target < nums[mid] { // 左边有序部分(注意=问题)
				r = mid - 1
			} else { // 右边可能有序，或者是部分有序
				l = mid + 1
			}
		} else { // 右边有序
			if nums[mid] < target && target <= nums[r] { // 右边有序部分(注意=问题)
				l = mid + 1
			} else { // 左边可能有序，或者是部分有序
				r = mid - 1
			}
		}
	}
	return -1
}

//func main() {
//	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 0))
//}
