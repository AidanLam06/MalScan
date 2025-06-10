# MalScan
A simple malware scanner to assess if a file may be malware 

## Features
- Hashes the target file and compares it against the MalwareBazaar database to check if the file is a known malware
- Checks the entropy of the file using the typical Shannon Entropy equation for bytes
--> $`H(X) = -\sum_{i} p(x_i) \log_2 p(x_i)`$
- Uses YARA rules (all taken from Neo23x0 YARA github) to check file heuristics

## Usage
You can use CLI or run it through a code editor with a terminal

CLI:
```powershell
cd "C:\your\download\location\MalScan"
python main.py
```
MalwareBazaar:
- To get a MalwareBazaar API key (needed for the program to check the file hash against MalwareBazaar database) you must go to their website, create an account and generate an Auth key.
- When you run this program you just paste your API key into the prompt that appears in the terminal
