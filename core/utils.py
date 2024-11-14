import binary2strings as b2s
from core.trieNode import Trie, insert_trie
from core.antiHashMap import AntiHashMap

def init():
    db = AntiHashMap()
    db.insert_file("C2ImplantSrc.exe", True)
    
    trie = Trie()
    
    insert_trie(trie, "strings.txt")
    return db, trie

# def extract_strings(filename):
    strings = []
    try:
        with open(filename, "rb") as i:
            data = i.read()
            for (string) in b2s.extract_all_strings(data):
                strings.append(string[0].strip())
    except Exception as e:
        return e
    
    return strings
    
def extract_strings(filebytes):
    strings = []
    try:
        all_strings = b2s.extract_all_strings(filebytes)
        for (string) in all_strings:
            strings.append(string[0].strip())
    except Exception as e:
        return e
    
    return strings