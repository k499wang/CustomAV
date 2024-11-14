import binary2strings as b2s
import argparse
from trieNode import Trie, insert_trie
from utils import extract_strings
import unittest
            
def main():
    trie = Trie()
    
    insert_trie(trie, "strings.txt")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filename",required=True)
    args = parser.parse_args()
    
    filename = args.filename
    matches = []
    
    strings = extract_strings(filename)
    # print(strings)

    
    for string in strings:
        match = trie.search_in_tree(string.strip().lower())
        if match:
            matches.append(match)   
    
    if matches:
        print(f"WE FOUND MALWARE: {matches}")
    else:
        print("CLEANNN")
        
main()