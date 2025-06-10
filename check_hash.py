import hashlib
import requests
import json

print("\nIf you are unfamiliar with how the MalwareBazaar API system works, see the README file on the github page where it is explained.")
api_key = input("Enter your MalwareBazaar API key: ").strip()
url = "https://mb-api.abuse.ch/api/v1/"

def compare_hash(file_path):
    sha = hashlib.sha_256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    hashed = sha.hexdigest()

    data = {"query" : "get_info", "hash" : hashed}
    headers = {"API-Key" : api_key}
    response = requests.post(url, data = data, headers = headers)
    
    if response.ok:
        print("\n\n************REQUEST SUCCESSFUL************")
        result = response.json()
        query_status = result.get("query_status")
        signature = result.get("data")[0].get("signature")
        if query_status == "ok":
            print(f"This file hash matches a known malware hash of type {signature}. Disconnect wifi and run antivirus scan immediately")
            while True:
                full = input("\nWould you like the full MalwareBazaar result (y/n): ").lower().strip()
                if full == "y":
                    print("\n", json.dumps(response.json(), indent=4)) 
                    return False
                elif full == "n":
                    return False
                else:
                    print("Invalid response. Try again\n")

    else:
        print("\n\n************REQUEST FAILED************")
        print(f"Error: {response.status_code} - {response.text}")

    
# def sampler():
#     hashed = "8A492973B12F84F49C52216D8C29755597F0B92A02311286B1F75EF5C265C30D"
#     data = {"query" : "get_info", "hash" : hashed}
#     headers = {"API-Key" : api_key}
#     response = requests.post(url, data = data, headers = headers)
    
#     if response.ok:
#         print("\n\n************REQUEST SUCCESSFUL************")
#         result = response.json()
#         query_status = result.get("query_status")
#         if query_status == "ok":
#             signature = result.get("data")[0].get("signature")
#             print(f"This file hash matches a known malware hash of type {signature}. Disconnect wifi and run antivirus scan immediately")
#             while True:
#                 full = input("\nWould you like the full MalwareBazaar result (y/n): ").lower().strip()
#                 if full == "y":
#                     print("\n", json.dumps(response.json(), indent=4))
#                     break
#                 elif full == "n":
#                     break
#                 else:
#                     print("Invalid response. Try again\n")
#         else:
#             print("prolly fine")

#     else:
#         print("\n\n************REQUEST FAILED************")
#         print(f"Error: {response.status_code} - {response.text}")


# sampler()