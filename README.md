# rolvs-password-checker
 Checks if given password has been made public before using the pwned checker api, and if it has, displays how many times.

Run main.py for the program with a tkinter gui.

Otherwise, run pass_check_script.py in the command line and provide any passwords you want checked as arguments.

Both options will encode your password with the hashlib library and only send the first 5 characters to the api, meaning your password will be safe.
