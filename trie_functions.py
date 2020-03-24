class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def trie_insert(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def trie_check(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                print(node.children[index])
                return False
            node = node.children[index] 

        return node != None and node.isEndOfWord

    def trie_print(self):
        words = []
        self._printer(self.root, '',  words)
        return words


    def _printer(self, node, word, words):
        if node.isEndOfWord:
            words.append(word)           
            
        for index, node in enumerate(node.children):
            if node:
                self._printer(node, word + chr(index+ord('a')) , words)
            

if __name__ == '__main__':
    words = ['kayak', 'kaki', 'kakima', 'kaka', 'kakababu','archi', 'archishman']
    trie = TrieTree()
    for word in words:
        trie.trie_insert(word)
    printed_words = trie.trie_print()
    print(printed_words)
    for word in printed_words:
        print(word, trie.trie_check(word))
    
