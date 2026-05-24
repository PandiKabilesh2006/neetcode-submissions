class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
        self.endWord=0
        self.cp=0
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
    
    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if(ch not in node.children):
                node.children[ch]=TrieNode()
            node=node.children[ch]
            node.cp+=1
        node.endOfWord=True
        node.endWord+=1
        
    def search(self, word: str) -> bool:
        def dfs(i, node):
            # reached end
            if i == len(word):
                return node.endOfWord
            ch = word[i]
            # wildcard
            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            # normal character
            if ch not in node.children:
                return False
            return dfs(i + 1, node.children[ch])
        return dfs(0, self.root)