class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # map a word to its frequency
        countMap = defaultdict(int)
        for word in words:
            countMap[word] += 1

        def insertTrieNode(root: TrieNode, word: str) -> None:
            cur = root
            for i in range(len(word)):
                ch = word[i]
                idx = ord(ch) - ord("a")
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()

                cur = cur.children[idx]
            cur.word = word

        # it's possible that whole list has the same words
        buckets = [[] for i in range(len(words) + 1)]
        for word, count in countMap.items():
            if not buckets[count]:
                buckets[count] = TrieNode()
            insertTrieNode(buckets[count], word)

        res = []
        def dfs(node: TrieNode):
            if node.word:
                res.append(node.word)

            if len(res) == k:
                return

            for child in node.children:
                if child:
                    dfs(child)

        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                dfs(buckets[i])
        return res

        