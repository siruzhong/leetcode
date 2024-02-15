package main

//func main() {
//	matrix := [][]int{
//		{1, 2},
//		{3, 4},
//	}
//	//matrix := [][]int{
//	//	{1, 2, 3},
//	//	{4, 5, 6},
//	//	{7, 8, 9},
//	//}
//	//matrix := [][]int{
//	//	{5, 1, 9, 11},
//	//	{2, 4, 8, 10},
//	//	{13, 3, 6, 7},
//	//	{15, 14, 12, 16},
//	//}
//	rotate(matrix)
//	fmt.Println(matrix)
//}

func rotate(matrix [][]int) {
	l := len(matrix)
	if l == 1 {
		return
	} else if l == 2 {
		swap(matrix, 0, 0, 0, 1)
		swap(matrix, 0, 0, 1, 1)
		swap(matrix, 1, 0, 0, 0)
	} else {
		for i := 0; i < l-2; i++ {
			for j := i; j < l-i-1; j++ {
				swap(matrix, i, j, j, l-i-1)
				swap(matrix, i, j, l-i-1, l-j-1)
				swap(matrix, l-j-1, i, i, j)
			}
		}
	}
}

func rotate2(matrix [][]int) {
	l := len(matrix)
	// 水平翻转
	for i := 0; i < l/2; i++ {
		for j := 0; j < len(matrix); j++ {
			matrix[i][j], matrix[l-i-1][j] = matrix[l-i-1][j], matrix[i][j]
		}
	}
	// 主对角线翻转
	for i := 0; i < l; i++ {
		for j := 0; j < i; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}

// swap 交换数组中两元素的值
func swap(matrix [][]int, x1, y1, x2, y2 int) {
	matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
}
