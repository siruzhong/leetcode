package main

import (
	"math"
	"sort"
)

func leastInterval(tasks []byte, n int) int {
	// 统计每个字母出现的次数
	count := make([]int, 26)
	for i := 0; i < len(tasks); i++ {
		count[tasks[i]-'A'] += 1
	}
	// 得到次数最多的字母
	sort.Ints(count)
	maxCount := count[25]
	// 计算还未填充其他字母的最小时间
	minLen := (n+1)*(maxCount-1) + 1
	// 填充剩余字母
	for i := 24; i >= 0; i-- {
		if count[i] == maxCount { // 如果某字母出现次数与maxCount一样，则需要+1，因为最后一个桶中多了该字母的任务
			minLen++
		}
	}
	// 如果所有冷却空格都填充满，则最短时间就是字母的长度
	return int(math.Max(float64(minLen), float64(len(tasks))))
}
