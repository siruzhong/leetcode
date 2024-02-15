package main

//func main() {
//	nums := []int{1, 2, 3}
//	nextPermutation(nums)
//	fmt.Println(nums)
//}

func nextPermutation(nums []int) {
	// 找到较小数的位置i
	i := len(nums) - 1
	for i >= 0 && nums[i-1] >= nums[i] {
		i--
	}
	i--	// 注意这里找到的是非降序左边的第一个元素,需要-1
	// 找到较大数的位置j
	if i >= 0 {
		j := len(nums) - 1
		for j > 0 && nums[i] >= nums[j] {
			j--
		}
		// 交换较小数和较大数
		nums[i], nums[j] = nums[j], nums[i]
	}
	// 反转i后面的数组
	reverse(nums[i+1:])
}

// reverse 数组反转
func reverse(nums []int) {
	for i, n := 0, len(nums); i < n/2; i++ {
		nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
	}
}
