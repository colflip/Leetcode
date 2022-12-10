# 127. 单词接龙
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        l = len(endWord)

        ws = set(wordList)

        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i + 1:]

                        if word in tail:
                            return res + 1

                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1

        return 0
