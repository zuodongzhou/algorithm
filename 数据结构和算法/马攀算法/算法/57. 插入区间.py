class Solution:
    def insert(self, intervals, newInterval):
        new_list = []
        l = newInterval[0]
        r = newInterval[1]
        flag = 0
        i = 0
        while i < len(intervals):
            if intervals[i][1] < l :
                new_list.append([intervals[i][0],intervals[i][1]])
                i += 1
            elif  intervals[i][0] > r:
                if flag == 0:
                    new_list.append([l,r])
                    flag = 1
                new_list.append([intervals[i][0], intervals[i][1]])
                i += 1
            else:
                j = i
                while j < len(intervals):
                    if  intervals[j][0] <= r:
                        l = min(l,intervals[j][0])
                        r = max(r,intervals[j][1])
                        j+= 1
                        if j == len(intervals):
                            flag = 1
                            new_list.append([l, r])
                            i = j
                    else:
                        i = j
                        break
        if i == 0 or flag == 0:
            new_list.append([l, r])
        return new_list
print(Solution().insert([],[2,5]))