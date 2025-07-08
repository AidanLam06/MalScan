import yara
import os
from constants import YARA_DIR

rules = os.listdir(YARA_DIR)

def ruleset_match(filepath):
    ruleset = {}
    for i, filename in enumerate(os.listdir(YARA_DIR)):
        if filename.endswith(".yar"):
            ruleset[filename[:-4]] = os.path.join(YARA_DIR, filename)

    rules = yara.compile(filepaths=ruleset)
    matches = rules.match(filepath)

    if len(matches) == 0:
        print("--> YARA clear")
        return False, None 
    else: 
        print("Hits:")
        for i, match in enumerate(matches):
            print(f"{i}) {match}")
        
        print("--> YARA hit")
        return True, matches

def match_diagnosis(matches):
    for i in matches:
        if "crime_ransom" in i:
            print("Ransomware was detected within this file. Disconnect from wifi and run antivirus scan immediately")
        else:
            print("this file contains code that is sometimes seen in malware. Upload the file to a more reputable scanner like VirusTotal for a more in-depth analysis of its contents.")