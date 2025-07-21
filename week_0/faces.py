"""
convert: accepts a str as input and returns that same input with
    - any :) converted to 🙂
    - Any :( converted to 🙁  
    - All other text should be returned unchanged.
"""
def convert(str):
    new_str = ""
    for i in str.split():
        if ":)" in str:
            new_str = str.replace(":)", "🙂")
        elif ":(" in str:
            new_str = str.replace(":(", "🙁")
        str = new_str
    return str


def main():
    prompt = input("Enter text: ")
    print(convert(prompt))

main()


