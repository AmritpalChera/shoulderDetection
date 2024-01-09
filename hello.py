from colorama import init, Fore

def say_hello(name):
    return f"Hello, {Fore.GREEN}{name}{Fore.RESET}!"

if __name__ == "__main__":
    init(autoreset=True)
    username = input("Enter your name: ")
    message = say_hello(username)
    print(message)