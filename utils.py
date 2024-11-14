import binary2strings as b2s
from trieNode import Trie, insert_trie


def extract_strings(filename):
    strings = []
    try:
        with open(filename, "rb") as i:
            data = i.read()
            for (string) in b2s.extract_all_strings(data):
                strings.append(string[0].strip())
    except Exception as e:
        return False
    
    return strings
        