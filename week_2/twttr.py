"""
Program that prompts the user for a str of text 
and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase
"""

def main():
    vowels = [
        "A", "E", "I", "O", "U", 
        "a", "e", "i", "o", "u"
        ]

    prompt = input("Input: ")
    new_str = ""

    for i in prompt:
        if not i in vowels:
            new_str += i
    print(f"Output: {new_str}")

main()