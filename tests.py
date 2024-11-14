import unittest 
from trieNode import Trie, insert_trie
from utils import extract_strings


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        
    def test_insert_search(self):
        curr = self.trie
        curr.insert("ASDF")
        
        self.assertEqual(curr.search("ASDF"), True)
    
    def test_insert_trie(self):
        curr = self.trie
        self.assertEqual(insert_trie(curr, "strings.txt"), True)
        
    def test_extract_strings(self):
        self.assertNotEqual(extract_strings("strings.txt"), False)
        
        
        

