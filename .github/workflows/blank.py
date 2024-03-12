import random
import calendar
from datetime import datetime

def get_input():
    names = []
    while True:
        name = input("Enter a name (or press Enter to stop): ")
        if not name:
            break
        names.append(name)
    random.shuffle(names)  # Randomly shuffle the list of names
    return names

def main():
    print("Welcome to the Name, Month, and Year Assigner!")
    print("Enter names. Press Enter with a blank name to finish.")

    names = get_input()

    if not names:
        print("No names entered. Exiting program.")
        return

    months = list(calendar.month_name)[1:]  # Remove empty string at index 0

    current_date = datetime.today()
    current_year = current_date.year
    current_month = current_date.month

    years = [current_year + (current_month + i - 1) // 12 for i in range(len(names))]

    print("\nAssigned month and year to names:")
    for i, name in enumerate(names, 0):
        month = months[(current_month + i - 1) % len(months)]
        year = years[i]
        print("{} - {} {}".format(name, month, year))

if __name__ == "__main__":
    main()
