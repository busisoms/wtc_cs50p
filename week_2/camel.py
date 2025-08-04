"""
Program that prompts the user for the name of a variable in
camel case and outputs the corresponding name in snake case.
"""

def main():
    prompt = input("camelCase: ")
    snake_case = ""
    
    for i in range(len(prompt)):
        snake_case += prompt[i].lower()
        if i != (len(prompt) - 1) and prompt[i + 1].isupper():
            snake_case += '_'
    print(f"snake_case: {snake_case}")

main()
            
            
