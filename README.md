# MalScan
A simple malware scanner to assess if a folder contains any files that may be malware 

## Features
- Hashes the target file and compares it against the MalwareBazaar database to check if the file is a known malware
- Checks the entropy of the file and flags files over a 7.4 entropy value
--> $`H(X) = -\sum_{i} p(x_i) \log_2 p(x_i)`$
- Uses YARA rules (all taken from Neo23x0 YARA github) to check file heuristics

## Usage
You can use CLI or run it through a code editor with a terminal

- Open up powershell
- Move to the directory you cloned this repository to
Then execute the following command:
```powershell
.\multifileScript.ps1 C:\folder\you\want\to\scan your-api-key
```

example:
```powershell
.\multifileScript.ps1 C:\malware_samples 537603393d31aae7ae5c66b51fe3558ee65bd2885d2dc433a8f7121f9a5b8c2d
```

## MalwareBazaar Setup
- To get a MalwareBazaar API key (needed for the program to check the file hash against MalwareBazaar database) you must go to their website, create an account and generate an Auth key.
- When you run this program you just paste your API key into the prompt that appears in the terminal
