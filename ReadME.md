# Introduction

This project demonstrates a proof-of-concept (POC) antivirus system that combines static and dynamic analysis techniques to detect malware. The system aims to showcase both traditional signature-based detection (via string matching) and runtime detection (through function hooking). 

- Static Analysis (String Searching): Compares uploaded strings or files against a predefined list of known malicious strings to identify threats at the file level.
- Dynamic Analysis (Function Hooking): Monitors process execution in real-time to detect suspicious activities that emerge during runtime, such as code injection or system manipulation.

# Getting Started

### Installation

Follow these simple steps to set up and run the antivirus system on your local machine.

1. Ensure you have Python 3.6+ installed. Then, install the necessary dependencies via pip:

```
pip install flask
pip install binary2strings
```

Once the dependencies are installed, run the main program using the following command from the root directory:
```
python3 main.py
```
The system will start a Flask server to handle the API endpoints.



### API Endpoints

#### POST /check_string

Upload a string to check it for malicious content. This performs a quick static analysis by matching the string against a list of known malicious signatures.

```
POST /check_string
Content-Type: application/json

{
  "data": "example_malicious_string"
}
```

#### POST /check_file: 

Upload a file to be analyzed for malicious content. The system performs both static and dynamic analysis to detect threats in the file's content and behavior.

```
POST /check_file
Content-Type: multipart/form-data

File: <file_to_analyze.exe>
```

Both endpoints compare the provided input against the strings.txt file located in the root directory. You can modify or add new strings to this file for customized testing.

# Testing the Antivirus

### Using the testFile.py Script

A dedicated script, testFile.py, is provided to test the antivirus functionality. This script uploads a file to the server and injects a DLL into the process for runtime analysis. This works be starting a suspended process, injecting the dll into it, and resuming it to avoid any race conditions.

### Running the Test Script

Execute the script using the following command(With the server running):

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

The antivirus uses two primary techniques to detect malware:

1. **Static Analysis**: During static analysis, the system scans the file for known malicious strings by comparing its content to the entries in strings.txt. This method is effective against simple malware that relies on signature-based detection.

2.**Dynamic Analysis**: Dynamic analysis involves monitoring the behavior of running processes. If a file attempts to inject malicious code, manipulate system resources, or perform any suspicious activity, the system detects it in real-time via function hooking.

3. **Evasion Techniques**: Advanced malware often uses techniques like unhooking to bypass detection. Files like UnhookedMally.exe demonstrate these challenges, highlighting the need for more advanced detection methods.


### Additional Notes

- Ensure the strings.txt file contains relevant malicious strings for testing.

- Modify and expand the strings.txt file to explore different detection scenarios.

- Use the endpoints and test script to analyze both predefined and custom files or strings.

# Conclusion

This POC antivirus system provides a foundational framework for malware detection using static and dynamic analysis techniques. It can be further enhanced by incorporating more advanced detection mechanisms and expanding the test cases.
