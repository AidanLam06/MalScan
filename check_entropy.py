import math
from collections import Counter

def find_entropy(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    if not data:
        return "file is empty"
    occurrence = Counter(data)
    file_len = len(data)
    entropy = 0.0
    for individual in occurrence.values():
        p = individual/file_len
        entropy += -(p*math.log2(p)) # Shannon Entropy of each individual byte added to a sum entropy 
    en = round(entropy, 2)
    if en >7.4:
        return True
    else:
        return False
