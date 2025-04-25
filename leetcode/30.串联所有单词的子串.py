from typing import List
from copy import deepcopy

#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#


# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_s, len_word, len_words = len(s), len(words[0]), len(words)
        res = []
        len_str = len_word * len_words
        map = dict()
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1


        # 将s划分为一个一个单词，从下标0~len_word-1划分即可
        for i in range(0, len_word):
            if len_s - i < len_str:
                return res
        
            # 深拷贝一份
            map_tmp=deepcopy(map)

            p, q = i, i + len_word
            while p < q and q <= len_s:
                tmp = s[q - len_word : q]
                if tmp in map_tmp and map_tmp[tmp] >= 1:
                    if q-p==len_str:
                        res.append(p)
                    map_tmp[tmp] -= 1
                    q += len_word
                else:
                    if q - p == len_word:
                        p = q
                        q += len_word
                    else:
                        map_tmp[s[p : p + len_word]] += 1
                        p += len_word

        return res


# print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
# @lc code=end
