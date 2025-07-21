# Calculate the tip amount

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    dollars_to_float: which should accept a str as input,
    remove the leading $,
    and return the amount as a float
    """
    return float(d[1:])


def percent_to_float(p):
    """
    percent_to_float: which should accept a str as input,
    remove the trailing %, 
    and return the percentage as a float
    """
    return float(p[:-1]) / 100


main()