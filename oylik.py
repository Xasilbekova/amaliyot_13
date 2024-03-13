class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        if salary >= 0:
            self.salary = salary
        else:
            raise ValueError("Ish xaqi 0dan kam bo'lishi mumkin emas.")

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.salary = new_salary
        else:
            raise ValueError("Ish xaqi 0dan kam bo'lishi mumkin emas.")

    def get_annual_salary(self):
        return self.salary * 12

if __name__ == "__main__":
    employee = Employee("Surayyo", 12345, 2500)
    print("Ismi:", employee.name)
    print("ID:", employee.emp_id)
    print("Oylik ish xaqqi:", employee.get_salary())
    print("Yillik ish xaqqi:", employee.get_annual_salary())
