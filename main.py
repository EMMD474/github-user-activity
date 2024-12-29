import get_event


def main():
    print("[GitHub User Activity]")

    user_command = input("Enter command: ")
    if user_command.startswith("github-activity"):
        parts = user_command.split()
        user_name = parts[1]

        get_event.get_events(user_name)
    else:
        print(f"[Error]: '{user_command}' is not a command")


if __name__ == "__main__":
    main()
