"""
Program that prompts the user for a greeting
    - If the greeting starts with “hello”, output $0
    - If the greeting starts with an “h” (but not “hello”), output $20
    - Otherwise, output $100
"""

def main():
    prompt = input("Greeting: ").strip().lower()

    if prompt.startswith("hello"):
        print("$0")
    elif not prompt.startswith("hello") and prompt.startswith("h"):
        print("$20")
    else:
        print("$100")
    
main()