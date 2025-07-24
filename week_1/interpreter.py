"""
program that prompts the user for an arithmetic expression and then calculates 
and outputs the result as a floating-point value formatted to one decimal place
"""

def add(x, z):
    """
    returns the sum of x and z
    """
    return x + z

def sub(x, z):
    """
    returns the diffence of x and z
    """
    return x - z

def mul(x, z):
    """
    returns the product of x and z
    """
    return x * z

def div(x, z):
    """
    returns the division of x and z
    """
    if z == 0:
        return "Error: can not divide by 0"
    return x / z

def main():
    prompt = input("Expression: ").split(' ')
    if len(prompt) < 3:
        print("Please enter a vaild expression")
        return
    
    x, y, z = prompt
    
    match y:
        case '+':
            result = add(float(x), float(z))
            print(result)
        case '-':
            result = sub(float(x), float(z))
            print(result)
        case '*':
            result = mul(float(x), float(z))
            print(result)
        case '/':
            result = div(float(x), float(z))
            print(result)
        case _:
            print("Please enter a vaild expression")

main()
