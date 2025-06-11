from check_entropy import find_entropy
from check_hash import compare_hash
import yara_check
import os

def main():
    print("DISCLAIMER: This project is not made by a professional and you should always use VirusTotal or another known and reputable scanner when dealing with malicious files. This program is extremely primitive and may miss advanced malware types.\n\n")
    
    filepath = input("Enter the path to the file you'd like to scan: ").strip()
    if os.path.exists(filepath):
        entropy = find_entropy(filepath)
        hash_match = compare_hash(filepath)
        match_bool, matches = yara_check.ruleset_match(filepath)

        if hash_match:
            print("This file has been reported on MalwareBazaar as confirmed malware. Disconnect from wifi and run antivirus scan immediately")
        elif match_bool:
            yara_check.match_diagnosis(matches)
        elif entropy and not hash_match and not match_bool:
            print("There is a chance that this file is malware. Upload file to VirusTotal file scanner for a more precise diagnosis")
        else:
            print("This file doesn't appear to be malware. However, if you are still concerned it may be malware, use the VirusTotal file scanner for a better analysis of its contents.")

    else:
        print("The file you specified doesn't exist or isn't seen by this program.")


if __name__ == "__main__":
    main()