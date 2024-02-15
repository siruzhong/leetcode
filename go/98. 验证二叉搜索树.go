package main

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 声明三个全局队列(注意这里的全局栈不能直接初始化，应该在类中初始化，详情:https://support.leetcode-cn.com/hc/kb/article/1194344/)
var nodes []*TreeNode
var uppers []int
var lowers []int

func isValidBST(root *TreeNode) bool {
	nodes = make([]*TreeNode, 0)
	uppers = make([]int, 0)
	lowers = make([]int, 0)
	// 为队列初始值(注意这里一定要为Int64，题目给的元素范围为[2^31~2^31-1],可能取道Int32的边界值)
	add(root, math.MinInt64, math.MaxInt64)
	// 深度搜索
	for len(nodes) > 0 {
		// 取出当前节点
		node, lower, upper := poll()
		if node == nil {
			continue
		}
		if node.Val <= lower || node.Val >= upper {
			return false
		}
		add(node.Left, lower, node.Val)  // 左节点校验
		add(node.Right, node.Val, upper) // 右节点校验
	}
	return true
}

// 模拟队列添加元素
func add(node *TreeNode, lower, upper int) {
	nodes = append(nodes, node)
	lowers = append(lowers, lower)
	uppers = append(uppers, upper)
}

// 模拟队列弹出元素
func poll() (node *TreeNode, lower, upper int) {
	if len(nodes) >= 1 {
		node = nodes[0]
		nodes = nodes[1:]
	}
	if len(uppers) >= 1 {
		upper = uppers[0]
		uppers = uppers[1:]
	}
	if len(lowers) >= 1 {
		lower = lowers[0]
		lowers = lowers[1:]
	}
	return
}

// 每次判断节点是否满足下界和上届的要求
func recurse(root *TreeNode, lower, upper int) bool {
	if root == nil {
		return true
	}
	if root.Val <= lower || root.Val >= upper {
		return false
	}
	return recurse(root.Left, lower, root.Val) && recurse(root.Right, root.Val, upper)
}

//func main() {
//	root := &TreeNode{Val: 2147483647}
//	root.Left, root.Right = nil, nil
//	fmt.Println(isValidBST(root))
//}
