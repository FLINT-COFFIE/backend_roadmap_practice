# Employee class
class Employee:
    # class variable
    tax_percentage = 0.055

    # initialize the class
    def __init__(self, first: str, last: str, pay: int):
        if pay < 0:
            raise ValueError("Pay cannot be negative")
        self.first = first
        self.last = last
        self.pay = pay

    # compute email
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    # compute fullname
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # assign tax_percent
    @classmethod
    def tax_percent(cls, percentage):
        cls.tax_percentage = percentage

    # compute net income
    def net_income(self):
        return self.pay * (1 - Employee.tax_percentage)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"Fullname: {self.fullname}\nEmail: {self.email}\nNet-Income: Ghc {float(self.net_income())}0\n"


if __name__ == "__main__":
    employee_1 = Employee("flint", "coffie", 4000)
    print(employee_1.email)
    print(employee_1.fullname)
    print(employee_1.net_income())
    print(employee_1)
