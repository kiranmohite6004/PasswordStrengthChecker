import re


def check_strength(password):
    if len(str(password)) < 8:
        return "Weak : Password should of at least 10 characters."
    elif not re.search(r"\d", password):
        return "Weak : Password should of at least 10 characters."
    elif not re.search(r"[A-Za-z]", password):
        return "Weak : Password should have at least a uppercase and lowercase character."
    elif not re.search(r"[!@#$%^&*()_+<>:?]", password):
        return "Weak : Password should of at least special character from [!@#$%^&*()_+<>:?]."
    else:
        return "Strong : Matches requirement."


pwd = input("Enter a password : ")
print(check_strength(pwd))
