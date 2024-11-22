"""
CP1404 - PRAC 07 - PROJECT MANAGEMENT
ESTIMATE: 2 HOURS5:11
ACTUAL:
"""
import datetime
from prac_07.project import Project

DEFAULT_FILENAME = 'projects.txt'
MENU_TEXT = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    """a"""
    print("Welcome to Pythonic Project Management")
    # {load_file(DEFAULT_FILENAME)}
    print(load_file(DEFAULT_FILENAME))
    print(f"Loaded projects from {DEFAULT_FILENAME}")
    print(MENU_TEXT)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            pass
        elif choice == 's':
            pass
        elif choice == 'd':
            pass
        elif choice == 'f':
            pass
        elif choice == 'a':
            pass
        elif choice == 'u':
            pass
        else:
            print("Invalid choice")
        print(MENU_TEXT)
        choice = input(">>> ").lower()

def load_file(filename):
    """Processes all data from input file."""
    projects = []
    with open(filename, 'r') as infile:
        infile.readline()
        number_of_records = 0
        for line in infile:
            number_of_records += 1
            parts = line.strip().split(',')
            print(parts)
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(parts[0], date, priority, cost, completion))
            print(projects)

        return number_of_records



main()