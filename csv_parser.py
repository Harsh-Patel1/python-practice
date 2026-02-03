import csv
def main(): 

    print("CSV Parser")
    # My code goes here
    with open('employees.csv', newline='') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
        

    # File automatically closes here, even if there's an error, 
    # the with statement closes the file without manually doing it,
    # Manual way you have to close it but if something crashes before
    # the file is closed, can forget and lead to problems (file corruption) 

    # TLDR: 'with' statement lets me open a file, use it, and AUTOMATICALLY close
    # It when the block ends, kinda like autosave on a video game

    # Part 2 Make your CSV parser ask the user which department they want to see, then only show employees from that department.
    user_input = input("Which department do you want to filter by?")
    with open('employees.csv', newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            if row[2].lower() == user_input.lower():
                print(row)
    




if __name__ == "__main__":
    main()