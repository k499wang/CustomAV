
# A trie is a tree-like data structure that stores a dynamic set of strings.
# Tries are commonly used to store the entire English language in a way that is more efficient compared to other data structures like a hash table. A trie is a tree structure where each node represents a single character of a string. Each node can have multiple children, and the path from the root to a node represents a string. The root node will have an empty string, and each child node represents a single character of a string.
# The trie data structure is used to store strings that can be searched in O(M) time complexity, where M is the length of the string.
class TrieNode:
    def __init__(self):
        self.children = {} # We will use a hashmap to store the children nodes, the key of the hashmap is some character from a-z, each character maps to some TrieNode
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode() # the root is a Trienode.
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children: 
                curr.children[c] = TrieNode() 
            
            curr = curr.children[c] # we skip to the next, becuase the character already exists in the trie.
                
        
        # Then we reach the end of the word
        curr.isEndOfWord = True
                
    
    # Note that we would have to make the string lowercase, this takes O(n) time.
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            
            else: # it is in children, so we want to go to that node and search for the rest of the word
                curr = curr.children[c]
        return True
    
    # Here, we are going to use a sliding window technique to search things for 
    def search_in_tree(self, text):
        matches = []
        l = 0
        
        for l in range(len(text)):
            curr = self.root # everytime, we want to go to the end
            for r in range(l, len(text)):
                c = text[r]
                if c not in curr.children:
                    break
                curr = curr.children[c]
                
                if curr.isEndOfWord:
                    matches.append(text[l:r+1]) 
                    l = r # sliding window!
                    break 
                    
        
        return matches
    
    
    # The time complexity is O(m*n), where m is the longest word in the trie
                    
                    
                
                
def insert_trie(trie, fileName):
    strings = []
    try:
        with open(fileName, "r") as i:
            for line in i: # we read this line by line
                word = line.strip().lower()
                trie.insert(word)
    except Exception as E:
        return False
    
    return True