from check_entropy import find_entropy
#from check_hash import compare_hash
import yara_check
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--apikey", required=True)

    args = parser.parse_args()

    entropy = find_entropy(args.file)
    #hash_match = compare_hash(args.file, args.apikey)
    match_bool = yara_check.ruleset_match(args.file)

    #if hash_match:
    #   print("CRITICAL RISK-Red")
    if match_bool:
        print("HIGH RISK-Orange")
    elif entropy and not match_bool: #elif entropy and not hash_match and not match_bool:
        print("MEDIUM RISK-Yellow")
    else:
        print("Clear-Green")

if __name__ == "__main__":
    main()