class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operator):
        if operator == "addition":
            return self.a + self.b
        elif operator == "subtraction":
            return self.a - self.b
        elif operator == "multiplication":
            return self.a * self.b
        elif operator == "division":
            if self.b == 0:
                return "Error: Division by zero"
            else:
                return self.a / self.b
        else:
            return "Operator is not correct"

a = float(input("1st number: "))
b = float(input("2nd number: "))
operator = input("Enter the Operation (addition/subtraction/multiplication/division): ")

calc = Calculator(a, b)
print("Result:", calc.calculate(operator))
