# imports
import time

from employee import Employee

# store employees
employees = {}


# functions
# option 1
def add_employee():
    # take inputs
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    try:
        pay = int(input("Enter pay amount: "))
    except ValueError:
        print("Employee not added")
        return

    # make index
    try:
        staff = Employee(first, last, pay)
    except ValueError:
        print("ValueError Pay cannot be negative")
        return
    employees[staff.fullname] = staff
    print("added employees")
    print(employees)


# option 2
def erase_employee():
    fullname = input("Enter Fullname: ")
    removed = employees.pop(fullname, None)
    if removed:
        print(f"Erased {removed.fullname} from staff records")
    else:
        print("No such employee")


# option 3
def print_details():
    fullname = input("Enter Fullname: ")
    if fullname in employees:
        print(employees[fullname])
    else:
        print("No such employee.")


# option 4
def total():
    print(f"Total number of employees: {len(employees)}")


def main():
    # Visuals
    print("==========================")
    print("===  Employee Manager  ===")
    print("==========================")

    # adding employees
    while True:
        # Inputs
        print("1. Add Employee\n")
        print("2. Erase Employee\n")
        print("3. Employee details\n")
        print("4. Total number of Employees\n")
        print("5. Exit\n")

        user_input = input("Enter your input: ")

        try:
            user_input = int(user_input)

        except ValueError:
            print("ValueError Incorrect Input")
            continue

        if user_input not in range(1, 6):
            print("Invalid option, choose 1-5.")
            continue

        elif user_input == 1:
            add_employee()

        elif user_input == 2:
            erase_employee()

        elif user_input == 3:
            print_details()

        elif user_input == 4:
            total()

        elif user_input == 5:
            print("Exiting...............")
            break

        time.sleep(2)


if __name__ == "__main__":
    main()
    # print(employees)
