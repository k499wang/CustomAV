from pyinjector import inject
import psutil
import sys
import os
import argparse 

def inject_file(process_name, dll_path):
    if not os.path.isabs(dll_path):
        dll_path = os.path.abspath(dll_path)

    # Find PID by process name
    pid = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name.lower():
            pid = proc.info['pid']
            break

    if pid is None:
        print(f"[!] Could not find process named {process_name}.")
        sys.exit(0)

    print(f"[+] Found PID: {pid}")
    print(dll_path)

    inject(pid, dll_path)

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-p', '--process', required=True)
    argparse.add_argument('-d', '--dll', required=True)
    
    args = argparse.parse_args()
    
    inject_file(args.process, args.dll)


