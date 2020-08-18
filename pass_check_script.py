import requests
import sys
import hashlib



def api_request(hash_password):
    url = "https://api.pwnedpasswords.com/range/" + hash_password
    re = requests.get(url)

    if re.status_code != 200:
        raise RuntimeError(f"Error fetching: {re.status_code}, check the api and try again.")

    return re


def get_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0



def api_check(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1[:5], sha1[5:]
    response = api_request(first5)
    return get_count(response, tail)



def main(args):
    for password in args:
        count = api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password")
        else:
            print(f"{password} was not found. Carry on.")
    return "Done!"



main(sys.argv[1:])











