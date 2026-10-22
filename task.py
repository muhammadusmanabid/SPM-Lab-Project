class students:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def calculate_percentage(self):
        return sum(self.marks)/len(self.marks)

    def check_result(self):
        percentage = self.calculate_percentage()

        if percentage >= 50:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.calculate_percentage()}%")
        print(f"Result: {self.check_result()}")

std1 = students("Muhammad Usman", "891-2023", [90, 89, 76, 79])
std2 = students("Muhammad Ayan", "917-2023", [80, 79, 76, 79])

std1.display()
std2.display()