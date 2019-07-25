import random

class ArrayProcessing:
    """ Class in which the functionality for task 1 is implemented """

    
    def __init__(self): # We generate an array during class initialization
        print("###### Start ######\n")
        self.initial_array = []
        for i in range(20):
            self.initial_array.append(random.randint(-10,10))
        print("Source array: {0}\n".format(self.initial_array))

    def task1_1(self):
        print("###### Task 1 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        max_negative = -10
        for x in array_for_process: # Find the maximum negative element
            if x < 0:
                if x > max_negative:
                    max_negative = x
        index_max_negative = array_for_process.index(max_negative) # We get its index
                    
        min_positive = 10
        for x in array_for_process: # Find the minimum negative element
            if x > 0:
                if x < min_positive:
                    min_positive = x
        index_min_positive = array_for_process.index(min_positive) # We get its index

        array_for_process.insert(index_max_negative, min_positive) #swapping...
        array_for_process.insert(index_min_positive, max_negative) #swapping...
        print("Modified array according to task 1.1: {0}\n".format(array_for_process))

    def task1_2(self):
        print("###### Task 2 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        summ = 0
        for i in range(20): # nothing to comment =)
            if i % 2 == 0:
                summ += array_for_process[i]
        print("The sum of the even elements of the array: {0}\n".format(summ))

    def task1_3(self):
        print("###### Task 3 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        for i in array_for_process: # nothing to comment ^_^
            if i < 0:
                index = array_for_process.index(i)
                del array_for_process[index]
                array_for_process.insert(index, 0)
        print("After replacing negative numbers with zeros: {0}\n".format(array_for_process))

    def task1_4(self):
        print("###### Task 4 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        for i in range(len(array_for_process) - 1): # too ez
            if array_for_process[i] > 0 and array_for_process[i+1] < 0:
                array_for_process[i] = array_for_process[i] * 3
        print("After tripling the positive elements facing the negative: {0}\n".format(array_for_process))

    def task1_5(self):
        print("###### Task 5 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        summ = 0
        for item in array_for_process: # nothing complicated
            summ += item
        avg = summ / len(array_for_process)
        result = min(array_for_process) - avg
        print("Arithmetic average: {0} \ Minimum: {1} \ Difference: {2}".format(avg, min(array_for_process), result))

    def task1_6(self):
        print("###### Task 6 ######\n")
        array_for_process = self.initial_array
        print("Source array: {0}\n".format(self.initial_array))
        for i in range(len(array_for_process)): # nothing complicated
            if i % 2 == 1 and array_for_process.count(i) > 1:
                print("Element {0} with index {1}".format(array_for_process[i], i))

a = ArrayProcessing()
a.task1_1()
a.task1_2()
a.task1_3()
a.task1_4()
a.task1_5()
a.task1_6()

