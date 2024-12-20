# Introduction
This project is a simple POC antivirus that has string searching and function hooking as it's features.

# Functionality

To run this antivirus, simply install the following packages

```
pip install flask
pip install binary2strings
```

Then run the file in the root directory of the project

```
python3 main.py
```

Then the following endpoitns will be available for you to upload any files/strings to check

```
check_string
check_file
```

Note the compares the strings to all the strings in the strings.txt file in the root directory of the folder. Feel free to add any strings if you wish to test anything out.

# Tests

You can test a singular file using the `testFile.py` folder in the project. This uploads the file to the server and then injects a dll into the process to dynamically detect any malicious strings in the program.

To do this, run:

```
testFile.py -f <filename>
```

There are 3 files that I have already provided in the project for you to test:

```
testFile.py -f C2ImplantSrc.exe
testFile.py -f BasicMally.exe
testFile.py -f UnhookedMally.exe
```

You will notice while running these files that the antivirus detects each file at different executions stages. C2ImplantSrc.exe being detected when the file is first uploaded to the server for checking, BasicMally.exe being detected during runtime from the inject dll, and UnhookMally.exe does not get detected at all. This is because each file employs different strategies and techniques to avoid analysis, and how these change how each file gets detected by the program.

For a basic rundown, The first file does not employ any special techniques at all, and follows the most basic structure that most malware in the wild have. Including dynamically allocating memory, copying the string to the memory space, and running some function. The second file uses Xor encryption to beat any static analysis, hence why it does not detected when strings are scanned against the file, but gets detected at runtime. The third file unhooks all the functions that have been hooked by the TestAvDLL.dll, hence rendering all the functionality useless.

The source code for all the malware and DLL can be found here:  https://github.com/k499wang/BasicMally, https://github.com/k499wang/TestAvDLL, https://github.com/k499wang/Injector.

