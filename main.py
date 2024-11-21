import binary2strings as b2s
import argparse
from core.trieNode import Trie, insert_trie
from core.utils import extract_strings
from app import create_app
from core.antiHashMap import AntiHashMap
from core.utils import init     
           
def main():
    db, trie = init()
    app = create_app(db, trie)
    app.run(host='127.0.0.1', debug=True)
           
main()         
            
# def main():
#     trie = Trie()
    
#     insert_trie(trie, "strings.txt")
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-f', "--filename",required=True)
#     args = parser.parse_args()
    
#     filename = args.filename
#     matches = []
    
#     strings = extract_strings(filename)
#     # print(strings)

    
#     for string in strings:
#         match = trie.search_in_tree(string.strip().lower())
#         if match:
#             matches.append(match)   
    
#     if matches:
#         print(f"WE FOUND MALWARE: {matches}")
#     else:
#         print("CLEANNN")
        
# main()