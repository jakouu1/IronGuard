import random
import string
import tkinter as tk

def is_strong_password(password):
    criteria_not_met = []
    if not any(char in string.punctuation for char in password):
        criteria_not_met.append("missing a special symbol")
    if not any(char.isdigit() for char in password):
        criteria_not_met.append("missing a number")
    if not any(char.isupper() for char in password):
        criteria_not_met.append("missing a capital letter")
    if len(password) < 8:
        criteria_not_met.append("less than 8 characters long")
    return len(criteria_not_met) == 0, criteria_not_met

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        new_password = ''.join(random.choice(characters) for _ in range(length))
        if is_strong_password(new_password)[0]:
            return new_password

def check_password(entry_password, canvas):
    password = entry_password.get()
    if not password:
        canvas.delete("all")
        return

    is_strong, criteria_not_met = is_strong_password(password)
    criteria_met = 4 - len(criteria_not_met)
    bar_width = 200
    section_width = bar_width / 4

    canvas.delete("all")
    for i in range(4):
        if i < criteria_met:
            color = "green"
        else:
            color = "red"
        x0 = i * section_width
        x1 = (i + 1) * section_width
        canvas.create_rectangle(x0, 0, x1, 30, fill=color, outline="")

def generate_new_password(selected_length, entry_new_password):
    try:
        length = int(selected_length)
    except ValueError:
        entry_new_password.delete(0, tk.END)
        entry_new_password.insert(0, "Invalid length")
        return
    new_password = generate_password(length)
    entry_new_password.delete(0, tk.END)
    entry_new_password.insert(0, new_password)

def choose_feature():
    root = tk.Tk()
    root.title("Iron Guard")
    root.geometry("300x150")

    def check_password_feature():
        root.destroy()
        display_password_checker()

    def generate_password_feature():
        root.destroy()
        display_password_generator()

    def quit_program():
        root.destroy()

    btn_check_password = tk.Button(root, text="Check Password", command=check_password_feature)
    btn_check_password.pack(pady=10)

    btn_generate_password = tk.Button(root, text="Generate Password", command=generate_password_feature)
    btn_generate_password.pack(pady=10)

    btn_quit = tk.Button(root, text="Quit", command=quit_program)
    btn_quit.pack(pady=10)

    root.mainloop()

def display_password_checker():
    root = tk.Tk()
    root.title("Password Checker")
    root.configure(bg="white")

    def go_back():
        root.destroy()
        choose_feature()

    label_password = tk.Label(root, text="Enter your password:", bg="white", fg="black", font=("Arial", 12))
    label_password.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_password = tk.Entry(root, show="*", font=("Arial", 12))
    entry_password.grid(row=0, column=1, padx=10, pady=5)

    canvas = tk.Canvas(root, width=200, height=30, bg="white")
    canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    entry_password.bind("<KeyRelease>", lambda event: check_password(entry_password, canvas))

    btn_back = tk.Button(root, text="Back", command=go_back)
    btn_back.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    root.mainloop()


def display_password_generator():
    root = tk.Tk()
    root.title("Password Generator")
    root.configure(bg="white")

    def go_back():
        root.destroy()
        choose_feature()

    def generate_password_with_length():
        selected_length = selected_length_var.get()
        generate_new_password(selected_length, entry_new_password)

    label_length = tk.Label(root, text="Select length of new password:", bg="white", fg="black", font=("Arial", 12))
    label_length.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    selected_length_var = tk.StringVar(root)
    selected_length_var.set("8")  # Default value

    length_options = [("8", "8"), ("16", "16"), ("32", "32")]

    for i, (value, length) in enumerate(length_options):
        tk.Radiobutton(root, text=length, variable=selected_length_var, value=value, bg="white", font=("Arial", 12)).grid(row=0, column=i+1, padx=5, pady=5, sticky="w")

    btn_generate_password = tk.Button(root, text="Generate Password", command=generate_password_with_length, bg="#008CBA", fg="white", font=("Arial", 12))
    btn_generate_password.grid(row=1, column=0, columnspan=len(length_options) + 1, padx=10, pady=5, sticky="ew")

    label_new_password = tk.Label(root, text="New Safe Password:", bg="white", fg="black", font=("Arial", 12))
    label_new_password.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_new_password = tk.Entry(root, font=("Arial", 12))
    entry_new_password.grid(row=2, column=1, columnspan=len(length_options), padx=10, pady=5)

    btn_back = tk.Button(root, text="Back", command=go_back)
    btn_back.grid(row=3, column=0, columnspan=len(length_options) + 1, padx=10, pady=5, sticky="ew")

    root.mainloop()

def generate_new_password(selected_length, entry_new_password):
    try:
        length = int(selected_length)
    except ValueError:
        entry_new_password.delete(0, tk.END)
        entry_new_password.insert(0, "Invalid length")
        return
    new_password = generate_password(length)
    entry_new_password.delete(0, tk.END)
    entry_new_password.insert(0, new_password)


def generate_new_password(selected_length, entry_new_password):
    try:
        length = int(selected_length)
    except ValueError:
        entry_new_password.delete(0, tk.END)
        entry_new_password.insert(0, "Invalid length")
        return
    new_password = generate_password(length)
    entry_new_password.delete(0, tk.END)
    entry_new_password.insert(0, new_password)


def main():
    choose_feature()

if __name__ == "__main__":
    main()
