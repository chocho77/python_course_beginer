def validate_username(username):
    if not username:
        return "Username cannot be empty."
    elif not username.isalnum():
        return "Username must contain only letters and numbers."
    else:
        return "Username is valid!"


def main():
    usernames = ["User123", "John_Doe", "hello!", "abc123", ""]

    for name in usernames:
        print(f"{name!r}: {validate_username(name)}")


if __name__ == '__main__':
    main()
