package main

type pair struct{ x, y int }

var directions = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // 上下左右

func exist(board [][]byte, word string) bool {
	// 二维数组的高度和宽度
	h, w := len(board), len(board[0])
	// 记录二位数组的节点是否被访问过
	visited := make([][]bool, h)
	for i := range visited {
		visited[i] = make([]bool, w)
	}
	// 函数check(i,j,k)表示判断以网格的(i,j)位置出发，能否搜索到单词word[k..]，其中word[k..]表示字符串word从第k个字符开始的后缀子串
	var check func(i, j, k int) bool
	check = func(i, j, k int) bool {
		if board[i][j] != word[k] { // 剪枝：当前字符不匹配
			return false
		}
		if k == len(word)-1 { // 单词存在于网格中
			return true
		}
		visited[i][j] = true
		defer func() { visited[i][j] = false }() // 回溯时还原已访问的单元格
		for _, dir := range directions {         // 上下左右
			if newI, newJ := i+dir.x, j+dir.y; 0 <= newI && newI < h && 0 <= newJ && newJ < w && !visited[newI][newJ] {
				if check(newI, newJ, k+1) {
					return true
				}
			}
		}
		return false
	}
	for i, row := range board {
		for j := range row {
			if check(i, j, 0) {
				return true
			}
		}
	}
	return false
}

//func main() {
//	board := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
//	fmt.Println(exist(board, "SEE"))
//}
