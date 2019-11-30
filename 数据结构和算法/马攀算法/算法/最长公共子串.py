

def find(s1,s2):
    #以 i j 结尾的最长子串，必须包括 ij
    if s1 == '' or s2 == '':
        return 0
    count = 0
    dp = [ [ 0 for j  in range(len(s2)+1)  ] for i in range(len(s1)+1) ]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            dp[i][j] = dp[i-1][j-1]+1  if s1[i-1] == s2[j-1] else 0
            if dp[i][j] > count:
                count = dp[i][j]
    return count
print(find('ecbced','ebabced'))

