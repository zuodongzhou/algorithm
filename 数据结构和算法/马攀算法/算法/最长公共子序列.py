def find(s1,s2):
    if s1 == '' or s2 == '':
        return 0
    count = 0
    dp = [ [ 0 for j  in range(len(s2)+1)  ] for i in range(len(s1)+1) ]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            dp[i][j] = max(dp[i-1][j-1] + (1 if s1[i-1] == s2[j-1] else 0),dp[i-1][j],dp[i][j-1])
            if dp[i][j] > count:
                count = dp[i][j]
    #path
    path =''
    for j in range(1,len(s2)+1):
        if dp[len(s1)][j] > dp[len(s1)][j-1]:
            path += s2[j-1]
    print(path)
    for i in dp:
        print(i)
    return count
print(find("ABCBDAB", "BDCABA"))