def run_system(config):
    mode = config.get("mode", "default")
    messages = config.get("messages", {})
    allow = config.get("allow_user_input", False)

    print(f"\n[MODE ACTIVE]: {mode}")
    print(messages.get("welcome", ""))

    if allow:
        data = input("\nInput something: ")
        print(f"You entered: {data}")

    print(messages.get("goodbye", ""))
