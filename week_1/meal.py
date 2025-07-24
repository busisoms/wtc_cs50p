"""
program that prompts the user for a time and outputs whether it’s:
- breakfast time,
- lunch time,
- or dinner time. 
If it’s not time for a meal, don’t output anything at all. 
"""

def main():
    prompt = input("What time is it? ").split(' ')
    time = float(convert(prompt))

    if len(prompt) == 2 and prompt[1] == 'p.m.':
        if time < 12:
            time += 12
    elif time == 12 and prompt[1] == 'a.m.':
        time -= 12

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    


def convert(time):
    """
    Converts time, a str in 24-hour/ 12-hour format,
    to the corresponding number of hours as a float.
    returns hours as float 
    """

    str_time = time[0].split(':')
    hours, mins = str_time
    hours = (float(mins) / 60) + float(hours)
    return hours


if __name__ == "__main__":
    main()