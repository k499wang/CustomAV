from pyinjector import inject
import psutil
import sys
import os


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <Process Name> <Path To DLL>")
    print(f"Eg: {sys.argv[0]} notepad.exe C:\\test\\messagebox.dll")
    sys.exit(0)

process_name = sys.argv[1]
dll_path = sys.argv[2]

# If the DLL path is relative, resolve it to an absolute path
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

inject(pid, dll_path)