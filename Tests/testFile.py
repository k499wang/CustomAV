import requests
import argparse
import os
import time
from inject import inject_file
import ctypes
from ctypes import windll
from ctypes import wintypes
import subprocess

CREATE_SUSPENDED = 0x00000004  # CREATE_SUSPENDED

# GOATED REFERENCE https://svn.python.org/projects/ctypes/trunk/ctypes/docs/manual/tutorial.html#loading-dynamic-link-libraries

class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD),
        ("lpReserved", wintypes.LPWSTR),
        ("lpDesktop", wintypes.LPWSTR),
        ("lpTitle", wintypes.LPWSTR),
        ("dwX", wintypes.DWORD),
        ("dwY", wintypes.DWORD),
        ("dwXSize", wintypes.DWORD),
        ("dwYSize", wintypes.DWORD),
        ("dwXCountChars", wintypes.DWORD),
        ("dwYCountChars", wintypes.DWORD),
        ("dwFillAttribute", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("wShowWindow", wintypes.WORD),
        ("cbReserved2", wintypes.WORD),
        ("lpReserved2", ctypes.POINTER(ctypes.c_byte)),
        ("hStdInput", wintypes.HANDLE),
        ("hStdOutput", wintypes.HANDLE),
        ("hStdError", wintypes.HANDLE),
    ]

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", wintypes.HANDLE),
        ("hThread", wintypes.HANDLE),
        ("dwProcessId", wintypes.DWORD),
        ("dwThreadId", wintypes.DWORD),
    ]


def upload_file(file_path, url):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    return response.status_code, response.json()

def start_suspended_process(executable_path):
    
    file_path = os.path.abspath(executable_path)
    
    si = STARTUPINFO()
    pi = PROCESS_INFORMATION()
    
    si.cb = ctypes.sizeof(STARTUPINFO)
    
    si.dwFlags = 0x00000001  # STARTF_USESHOWWINDOW
    si.wShowWindow = 0x00000000  # SW_HIDE

    process_handle = ctypes.windll.kernel32.CreateProcessW(
            file_path,
            None,
            None,
            None,
            False,
            CREATE_SUSPENDED,
            None,
            None,
            ctypes.byref(si), # we pass a value by reference
            ctypes.byref(pi)
    )

    if not process_handle:
        raise ctypes.WinError()

    return pi

    
    
if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-f', '--file', required=True)
    
    args = argparse.parse_args()
    
    
    url = 'http://localhost:5000/check_file'
    file_path = args.file
    dll_path = os.path.abspath("TestAvDLL.dll")
    
    status_code, response = upload_file(file_path, url)
    
    if status_code == 201:
        print("Malicious File, Matches: ", response)
    else:
        print("File is Clean ... For now.")
        
    # We then Start a suspended process DLL here
    
    print("Starting Suspended Process")
    proc_info = start_suspended_process(file_path)
    
    # Inject the DLL
    print("Injecting DLL")
    inject_file(file_path, "TestAvDLL.dll")

    
    # Resume the Process
    
    windll.kernel32.ResumeThread(proc_info.hThread)

    
    
    try:
        print("Process running. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        
        windll.kernel32.CloseHandle(proc_info.hProcess)
        windll.kernel32.CloseHandle(proc_info.hThread)
        windll.kernel32.TerminateProcess(proc_info.hProcess, 0)

        
        
