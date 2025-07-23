import re

def main():
    while True:
        email = get_user_input()
        if vailidate_user_input(email, r"^.+@[^@]+\.edu$"):
            print("Valid")
            break
        else:
            print("Invalid")

def get_user_input() -> str:
    e = input("Enter your email: ").strip()
    return e

def vailidate_user_input(e: str, regular_expression: str) -> bool:
    return True if re.search(regular_expression, e) else False


if __name__ == "__main__":
    main()