import tkinter as tk
from tkinter import ttk
import requests
import hashlib


#functions

def pass_api_request(hash_password):
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


def pass_api_check(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1[:5], sha1[5:]
    response = pass_api_request(first5)
    return get_count(response, tail)


def pass_check(password):
    if password == "":
        console["text"] = "Please enter a password first"
        return 0
    entry.delete(0, "end")
    console["text"] = f"Checking if {password} has been pwned..."
    count = pass_api_check(password)
    if count:
        console["text"] = f"Check complete\n\nThe password was found: {str(count)} times\n\nA new password is recommended"
    else:
        console["text"] = "Check complete\n\nThe password was not found\n\nA new password is not required"


#Email checking requires an api key from Have I Been Pwned api
##################
# def email_check(email):
#     url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + str(email) + "?includeUnverified=true"
#     re = requests.get(url, verify=True)
#
#     if re.status_code != 200:
#         raise RuntimeError(f"Error fetching: {re.status_code}, check the api and try again.")
#     else:
#         print(re)
################


#start of gui
root = tk.Tk()

#Set icon and title for window
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./icon.ico'))
root.title("Pwned Password Checker")

#Canvas to define default window size
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

#background
bg_label = tk.Label(root, bg="black")
bg_label.place(relwidth=1, relheight=1)

#Making the frames
title_frame = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

#Placing Frames
title_frame.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)
frame2.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.2)
frame3.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.45)

#Title
title_label = tk.Label(title_frame, text="Pwned Password Checker", font=("Helvetica", 14, "underline", "bold"), bg="Black", fg="yellow")
title_label.place(relwidth=0.99, relheight=0.9, relx=0.005, rely=0.05)

#entry label
entry = ttk.Entry(frame2, background="gray", font=("Times", 14), justify="center")
entry.place(relwidth=0.6, relheight=0.9, relx=0.005, rely=0.05)

#entry button
password_submit = ttk.Button(frame2, text="Check password", command=lambda: pass_check(entry.get()), cursor="hand2")
password_submit.place(relwidth=0.385, relheight=0.9, relx=0.61, rely=0.05)

#Console
console = ttk.Label(frame3, background="black", foreground="yellow", text="The program is ready for use.\n\nPlease enter a password above and\nclick the 'Check password' button to check\nif your password has been pwned.\n\nDon't worry, as only a small, encrypted\nfragmentof your password is sent over\nthe web, so your password is secure.", justify="left", font=("Helvetica", 14), pad=10, anchor="nw")
console.place(relwidth=0.99, relheight=0.99, relx=0.005, rely=0.005)

root.mainloop()