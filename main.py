import sys

# Example of the main module
def main():
    print("Welcome to LoopForge!")

    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        print(f"[+] Your prompt: {user_prompt}")
    else:
        print("[+] No prompt found. Please provide a prompt.")
    
if __name__ == "__main__":
    main()

