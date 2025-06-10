# MalScan
A simple malware scanner to assess if a file may be malware 


## Features
- Hashes the target file and compares it against the MalwareBazaar database to check if the file is a known malware
- Checks the entropy of the file using the typical Shannon Entropy equation for bytes
$$
H(X) = -\sum_{i} p(x_i) \log_2 p(x_i)
$$
