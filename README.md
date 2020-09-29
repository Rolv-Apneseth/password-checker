# password-checker
 Checks if given password has been made public before by using the pwned checker api, and if it has, displays how many times.

## What I learned
* Building GUI's using tkinter
* Interaction with a public api
* Use of the hashlib library for SHA1 encoding of information 
* Handling user data with responsibility

## Installation
1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/).
2. Clone the repository by opening your command line/terminal and run: ```git clone https://github.com/Rolv-Apneseth/password-checker.git```
    * Note: if you don't have git, it can be downloaded from [here](https://git-scm.com/downloads).
3. Install the requirements for the program.
    * In your terminal, navigate to the cloned directory and run: 
    ```python3 -m pip install -r requirements.txt```
4. To run the actual program, navigate further into the password-checker folder and from that directory run: ```python3 main.py```

## Usage
1. After running main.py, click on the entry box and type in any password you would like checked
2. Click on the check password button. Your results will be displayed on the bottom part of the program.

Alternatively, run pass_check_script.py in the terminal/command line and provide any passwords you want checked as arguments.

Unfortunately, to check emails which have been leaked, an api key is required. If you wish to just check a personal email, however, you can easily do so by visiting their [website](https://haveibeenpwned.com/)

## Security
Both options will encode your password with the hashlib library and only send the first 5 characters of this encoded string to the public api.

The api then returns many matches they have for those first 5 characters and this program matches the given password to the ones received from the api to get a count.

These steps mean that your password will be completely safe, as the api will only have access to a small part of it and the program does not save any data.
