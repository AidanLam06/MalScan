import math
from collections import Counter
import sys

def find_entropy(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
    except PermissionError:
        print("The file path must lead to a file. Perhaps you've specified the location to a folder or a file that requires admin permissions to access?")
        sys.exit(0)

    occurrence = Counter(data)
    file_len = len(data)
    entropy = 0.0
    for individual in occurrence.values():
        p = individual/file_len
        entropy += -(p*math.log2(p)) # Shannon Entropy of each individual byte added to a sum entropy 
    en = round(entropy, 2)
    if en >7.4:
        print("--> Entropy hit")
        return True
    else:
        print("--> Entropy clear")
        return False