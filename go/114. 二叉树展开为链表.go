package main

var list []int

func flatten(root *TreeNode) {
	list = make([]int, 0)
	if root == nil {
		return
	}
	preOrder(root)
	if len(list) == 1 {
		root.Left, root.Right = nil, nil
		return
	} else {
		for i := 1; i < len(list); i++ {
			root.Left = nil
			root.Right = &TreeNode{Val: list[i]}
			root = root.Right
		}
	}
}

func preOrder(root *TreeNode) {
	if root == nil {
		return
	}
	list = append(list, root.Val)
	preOrder(root.Left)
	preOrder(root.Right)
}

//func main() {
//	root := &TreeNode{Val: 0}
//	//node1 := &TreeNode{Val: 2}
//	//node2 := &TreeNode{Val: 5}
//	//node3 := &TreeNode{Val: 3}
//	//node4 := &TreeNode{Val: 4}
//	//node5 := &TreeNode{Val: 6}
//	//root.Left = node1
//	//root.Right = node2
//	//node1.Left = node3
//	//node1.Right = node4
//	//node2.Right = node5
//	flatten(root)
//	fmt.Println(root)
//}
