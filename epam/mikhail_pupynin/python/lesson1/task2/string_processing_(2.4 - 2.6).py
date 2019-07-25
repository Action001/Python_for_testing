from itertools import groupby

class StringProcessing:
    """ Class in which the functionality for tasks 2.4 - 2.6 is implemented"""
    def __init__(self):
        print("###### Start ######\nUse 'STOP' to stop entering strings\n")
        self.strings = []
        while True:
            string = input("Enter a word: ")
            if string == "STOP":
                break
            else: self.strings.append(string)
        print("\nOur words: {0}\n".format(self.strings))

    def task2_4(self):
        print("###### Task 4 ######\n")
        global_count = 10000
        global_index = 0
        for string in self.strings:
            letters = []
            for let in string:
                letters.append(let)
            count = len(list(set(letters))) # Удаляем дубликаты из массива и получаем его длину
            if count < global_count:
                global_count = count
                global_index = self.strings.index(string)
        print("The number of different characters is minimal in a word: {0}\n".format(self.strings[global_index]))

    def task2_5(self):
        print("###### Task 5 ######\n")
        for string in self.strings:
            letters = []
            for let in string:
                letters.append(let)
            count = len(list(set(letters))) #Удаляем дубликаты из массива и получаем его длину
            if len(letters) == count:
                print("A word that consists only of various characters: {0}\n".format(string))
                break
        else: print("No string consisting only of different characters\n")

    def task2_6(self):
        print("###### Task 6 ######\n")
        isdigit_words = []
        for string in self.strings:
            if string.isdigit():
                isdigit_words.append(string)
        if len(isdigit_words) == 0:
            print("Not a single word consists only of numbers\n")
        elif len(isdigit_words) == 1:
            print("A word that consists only of numbers: {0}\n".format(isdigit_words[0]))
        else: print("A word that consists only of numbers: ".format(isdigit_words[1]))

a = StringProcessing()
a.task2_4()
a.task2_5()
a.task2_6()


