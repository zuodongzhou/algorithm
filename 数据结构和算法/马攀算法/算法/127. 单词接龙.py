class Solution(object):
    # 本题采用广度遍历方法
    def ladderLength(self, beginWord, endWord, wordList):
        # 首先给wordList列表中单词去重
        word_set = set(wordList)
        # 定义当前层的单词集合为beginWord
        cur_word = [beginWord]
        # 定义下一层的单词集合
        next_word = []
        # 定义从 beginWord 到 endWord 的最短转换序列的长度
        depth = 1
        while cur_word:
            for word in cur_word:
                # 如果endWord出现在当前层的cur_word单词集合中，则立即返回该深度
                if word == endWord:
                    return depth
                for index in range(len(word)):
                    for indice in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:index]+indice+word[index+1:]
                        if new_word in word_set:
                            word_set.remove(new_word)
                            next_word.append(new_word)
            # 如果endWord未出现在当前层的cur_word单词集合中，则深度+1
            depth += 1
            cur_word = next_word
            next_word = []
        return 0
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sequence_length = Solution().ladderLength(beginWord, endWord, wordList)
    print(sequence_length)
