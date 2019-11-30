'''
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。

'''
'''贪心
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        if not intervals:
            return 0
        cur_r = intervals[0][1]

        for l, r in intervals[1:]:
            if l >= cur_r:
                cur_r = r
            else:
                if r >= cur_r:
                    count += 1
                else:
                    count += 1
                    cur_r = r
        return count