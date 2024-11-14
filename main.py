import binary2strings as b2s
import argparse
from trieNode import Trie, insert_trie
from utils import extract_strings
import unittest


            
def main():
    trie = Trie()
    
    insert_trie(trie, "strings.txt")
    print(trie.search("MALWARE"))
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filename",required=True)
    args = parser.parse_args()
    
    filename = args.filename
    
    strings = extract_strings(filename)
        
    
    
        
main()