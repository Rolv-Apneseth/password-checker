import os
import tkinter as tk
from tkinter import ttk

import pass_check_script


# COLOURS
BG_PRIMARY = "#1F1B24"
BG_SECONDARY = "#373040"
FG = "#cccccc"

# FONTS
CONSOLE_FONT = ("Helvetica", 14)
TITLE_FONT = ("Helvetica", 18, "bold")


def pass_check(password):
    """
    Calls api_check from pass_check_script.py and changes gui elements as
    the process is carried out.
    """

    # Return if no password was given
    if password == "":
        console["text"] = "Please enter a password first"
        return

    # Clear entry element
    entry.delete(0, "end")

    count = pass_check_script.api_check(password)
    if count:
        console["text"] = (
            f"Check complete\n\nThe password was found: {str(count)} times"
            "\n\nA new password is recommended"
        )
    else:
        console["text"] = (
            "Check complete\n\nThe password was not found\n\n"
            "A new password is not required"
        )


# GUI
root = tk.Tk()

# Set icon and title for window
root.tk.call(
    "wm",
    "iconphoto",
    root._w,
    tk.PhotoImage(file=os.path.join(os.getcwd(), "assets/icon.ico")),
)
root.title("Pwned Password Checker")

# Canvas to define default window size
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

# Background
bg_label = tk.Label(root, bg=BG_PRIMARY)
bg_label.place(relwidth=1, relheight=1)

# Making the frames
title_frame = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

# Placing Frames
title_frame.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)
frame2.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.2)
frame3.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.45)

# Title
title_label = tk.Label(
    title_frame,
    text="Pwned Password Checker",
    font=TITLE_FONT,
    bg=BG_SECONDARY,
    fg=FG,
)
title_label.place(relwidth=1, relheight=1, relx=0, rely=0)

# Entry label
entry = ttk.Entry(frame2, background="gray", font=("Times", 14), justify="center")
entry.place(relwidth=0.6, relheight=0.9, relx=0.005, rely=0.05)

# Entry button
password_submit = ttk.Button(
    frame2,
    text="Check password",
    command=lambda: pass_check(entry.get()),
    cursor="hand2",
)
password_submit.place(relwidth=0.385, relheight=0.9, relx=0.61, rely=0.05)

# Console
console = ttk.Label(
    frame3,
    background=BG_SECONDARY,
    foreground=FG,
    text=(
        "The program is ready for use.\n\nPlease enter a password above "
        "and\nclick the 'Check password' button to check\nif your password "
        "has been pwned.\n\nDon't worry, as only a small, encrypted\n"
        "fragmentof your password is sent over\nthe web, so your password "
        "is secure."
    ),
    justify="left",
    font=CONSOLE_FONT,
    pad=10,
    anchor="nw",
)
console.place(relwidth=1, relheight=1, relx=0, rely=0)

root.mainloop()
