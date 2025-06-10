import yara
import os

ruledir = "yara"

def ruleset_match(filepath):
    ruleset = {}
    for i, filename in enumerate(os.listdir(ruledir)):
        if filename.endswith(".yar"):
            ruleset[filename[:-4]] = os.path.join(ruledir, filename)

    rules = yara.compile(filepaths=ruleset)
    matches = rules.match(filepath)

    if len(matches) == 0:
        return False, None 
    else: 
        print("Hits:")
        for i, match in enumerate(matches):
            print(f"{i}) {match}")
        return True, matches

def get_ruleset():
    ruleset = [i for i in (os.listdir(ruledir)) if i.endswith(".yar")]
    return ruleset

def match_diagnosis(matches):
    for i in matches:
        if "crime_ransom" in i:
            print("Ransomware was detected within this file. Disconnect from wifi and run antivirus scan immediately")
        elif "thor_inverse_matches" in i:
            print("This file contains suspicious code. Run antivirus scan and upload to VirusTotal file scanner for a more precise diagnosis")
        else:
            print("this file contains code that is sometimes seen in malware. Upload the file to a more reputable scanner like VirusTotal for a more in-depth analysis of its contents.")