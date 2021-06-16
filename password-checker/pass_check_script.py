import requests
import sys
import hashlib


def api_request(hash_password):
    """
    Sends first 5 characters of an encoded SHA-1 password to the pwned
    checker api, which then returns tail ends of encoded passwords
    which matched the first 5 characters sent.
    """

    url = "https://api.pwnedpasswords.com/range/" + hash_password
    re = requests.get(url)

    if re.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {re.status_code}, check the api and try again."
        )

    return re


def get_count(hashes, hash_to_check):
    """
    Counts encoded tail ends of passwords which match given tail end
    of password being checked.
    """

    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def api_check(password):
    """
    Encodes password given with SHA-1 using the hashlib library.

    Gets the response from api with only the first 5 characters
    of the encoded password, so that the whole password is not
    sent over the internet.

    From the tail ends of encoded passwords returned by the
    api_request, the tail ends which match that of the encoded
    password are counted and returned as a number.
    """

    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1[:5], sha1[5:]
    response = api_request(first5)

    return get_count(response, tail)


def format_password(password):
    """
    Formats password for printing to the terminal.

    This is done so that the password is not returned as plain text.
    """

    return password[0] + "*" * (len(password) - 1)


if __name__ == "__main__":
    for password in sys.argv[1:]:
        count = api_check(password)

        password = format_password(password)

        if count:
            print(
                f"\n{password} was found {count} times... you "
                "should probably change your password"
            )
        else:
            print(f"\n{password} was not found. Carry on.")
