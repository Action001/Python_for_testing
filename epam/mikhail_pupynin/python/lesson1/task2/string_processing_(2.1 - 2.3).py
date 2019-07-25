class StringProcessing:
    """ Class in which the functionality for tasks 2.1 - 2.3 is implemented """

    
    def __init__(self):
        print("###### Start ######\nUse 'STOP' to stop entering strings\n")
        self.strings = []
        while True:
            string = input("Enter a string: ")
            if string == "STOP":
                break
            else: self.strings.append(string)
        print("Our strings: {0}\n".format(self.strings))

    def task2_1(self):
        print("###### Task 1 ######\n")
        index1 = 0
        index2 = 0
        minn = 99999
        maxx = 0
        for string in self.strings:
            if len(string) > maxx:
                maxx = len(string)
                index1 = self.strings.index(string)
            if len(string) < minn:
                minn = len(string)
                index2 = self.strings.index(string)
        print("Short: {0}\tIts lenght: {1}\nLong: {2}\tIts length: {3}\n".format(self.strings[index2],
                            len(self.strings[index2]), self.strings[index1], len(self.strings[index1])))

    def task2_2(self):
        print("###### Task 2 ######\n")
        summ = 0
        for string in self.strings:
            summ += len(string)
        avg = summ / len(self.strings)
        print("\tAverage Length: {0}\n".format(avg))
        for string in self.strings:
            if len(string) > avg:
                print("Line:{0}\tIts length: {1}".format(string, len(string)))

    def task2_3(self):
        print("\n###### Task 3 ######\n")
        summ = 0
        for string in self.strings:
            summ += len(string)
        avg = summ / len(self.strings)
        print("\tAverage Length: {0}\n".format(avg))
        for string in self.strings:
            if len(string) < avg:
                print("String: {0}\tIts lenght: {1}".format(string, len(string)))

a = StringProcessing()
a.task2_1()
a.task2_2()
a.task2_3()

