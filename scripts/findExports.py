import pefile
import sys
import argparse
import os



def find_exports(file_path):
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
        
    pe = pefile.PE(file_path)
    exports = []
    for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        exports.append(entry.name.decode('utf-8'))
    return exports

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-f', '--file', required=True)
    
    args = argparse.parse_args()
    imports = find_exports(args.file)
    
    for impt in imports:
        print(impt)