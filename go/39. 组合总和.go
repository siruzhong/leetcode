package main

func combinationSum(candidates []int, target int) (ans [][]int) {
	var comb []int
	var dfs func(target, id int)
	dfs = func(target, id int) {
		if id == len(candidates) {
			return
		}
		if target == 0 {
			ans = append(ans, append([]int{}, comb...)) // 注意这里二维切片append一维切片的写法
			return
		}
		// 跳过当前数
		dfs(target, id+1)
		// 选择当前数
		if target-candidates[id] >= 0 {
			comb = append(comb, candidates[id])
			dfs(target-candidates[id], id)
			comb = comb[:len(comb)-1] // comb删除当前数字
		}
	}
	dfs(target, 0)
	return
}

//func main() {
//	candidates := []int{2, 3, 6, 7}
//	fmt.Println(combinationSum(candidates, 7))
//}
