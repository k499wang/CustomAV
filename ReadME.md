# Introduction

This project demonstrates a simple proof-of-concept (POC) antivirus system. The key features include:

- String Searching: Detects malicious strings by comparing them to a predefined list.

- Function Hooking: Dynamically monitors and detects suspicious activities during runtime.

# Getting Started

### Installation

To set up and run the antivirus, follow these steps:

Install the required dependencies:
```
pip install flask
pip install binary2strings
```
Run the main program from the root directory:
```
python3 main.py
```
API Endpoints

Once the program is running, the following endpoints will be available for use:

- POST /check_string: Upload a string to check for malicious content.

- POST /check_file: Upload a file to analyze its content.

The system compares the provided input against a list of strings stored in the strings.txt file located in the root directory. You can modify or add new strings to this file to test additional scenarios.

# Testing the Antivirus

### Using the testFile.py Script

A dedicated script, testFile.py, is provided to test the antivirus functionality. This script uploads a file to the server and injects a DLL into the process for runtime analysis.

### Running the Test Script

Execute the script using the following command:

```
python3 testFile.py -f <filename>
```
### Pre-Provided Test Files

The project includes three test files to demonstrate different detection scenarios:

- C2ImplantSrc.exe: Detected during file upload.

The antivirus identifies malicious strings at the static analysis stage.

- BasicMally.exe: Detected during runtime.

The injected DLL detects malicious strings while the program is running.

- UnhookedMally.exe: Not detected.

This file uses unhooking to evade analysis, bypassing detection mechanisms.

Example Commands

```
python3 testFile.py -f C2ImplantSrc.exe
python3 testFile.py -f BasicMally.exe
python3 testFile.py -f UnhookedMally.exe
```

### How Detection Works

Each test file employs unique strategies to evade detection, showcasing the antivirus's strengths and limitations:

Static Analysis: Effective for files like C2ImplantSrc.exe with identifiable malicious strings.

Dynamic Analysis: Detects runtime activities, as shown with BasicMally.exe.

Evasion Techniques: Files like UnhookedMally.exe demonstrate the challenges of detecting sophisticated malware.

### Additional Notes

- Ensure the strings.txt file contains relevant malicious strings for testing.

- Modify and expand the strings.txt file to explore different detection scenarios.

- Use the endpoints and test script to analyze both predefined and custom files or strings.

# Conclusion

This POC antivirus system provides a foundational framework for malware detection using static and dynamic analysis techniques. It can be further enhanced by incorporating more advanced detection mechanisms and expanding the test cases.
