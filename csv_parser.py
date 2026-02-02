import csv
def main(): 

    print("CSV Parser")
    # My code goes here
    with open('employees.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    # File automatically closes here, even if there's an error, 
    # the with statement closes the file without manually doing it,
    # Manual way you have to close it but if something crashes before
    # the file is closed, can forget and lead to problems (file corruption) 

    # TLDR: 'with' statement lets me open a file, use it, and AUTOMATICALLY close
    # It when the block ends, kinda like autosave on a video game



if __name__ == "__main__":
    main()