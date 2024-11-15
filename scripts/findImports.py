import pefile
import sys
import argparse
import os



def find_imports(file_path):
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
        
    pe = pefile.PE(file_path)
    imports = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        for imp in entry.imports:
            imports.append(imp.name.decode('utf-8'))
    return imports

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-f', '--file', required=True)
    
    args = argparse.parse_args()
    imports = find_imports(args.file)
    
    for impt in imports:
        print(impt)