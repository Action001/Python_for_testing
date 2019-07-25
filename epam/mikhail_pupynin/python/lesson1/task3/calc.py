class Calculator():
    """ In this class, a calculator is implemented """

    
    def __init__(self):
        print("""
\t The calculator supports only 4 operations ("+","-","*","/")
\t Expression example: 1 + 1, 2 * 5, 12 / 14, 100 - 99
\t Attention, separate numbers and operands with spaces\n""")
        while True:
            exp = input("Enter expression: ")
            try:
                self.a = int(exp.split(" ")[0])
                self.b = int(exp.split(" ")[2])
            except:
                print("""The expression was entered incorrectly
     Please try again""")
            if exp.split(" ")[1] == "+":
                print(exp + " = " + str(Calculator.__add(self)))
            elif exp.split(" ")[1] == "-":
                print(exp + " = " + str(Calculator.__sub(self)))
            elif exp.split(" ")[1] == "*":
                print(exp + " = " + str(Calculator.__mul(self)))
            elif exp.split(" ")[1] == "/":
                print(exp + " = " + str(Calculator.__div(self)))
        
    def __add(self):
        return self.a + self.b

    def __sub(self):
        return self.a - self.b

    def __mul(self):
        return self.a * self.b

    def __div(self):
        return self.a / self.b

calc = Calculator()
