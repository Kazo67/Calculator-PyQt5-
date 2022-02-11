import math


class Helper:
    @staticmethod
    def add_symbol_at_the_end_of_label(string, symbol):
        numbers = [
            '0', '1', '2',
            '3', '4', '5',
            '6', '7', '8',
            '9'
        ]
        if (symbol != "."):
            if (symbol != "0"):
                if len(string) > 0:
                    for number in numbers:
                        if (string[-1] == number):
                            string += symbol
                return string
            if (symbol == "0"):
                string += symbol
                return string

        if (symbol == "."):
            lastCharOfStringIsNumber = False
            if len(string) > 0:
                for number in numbers:
                    if (string[-1] == number):
                        lastCharOfStringIsNumber = True
                        foundPoint = False
                if (lastCharOfStringIsNumber == True):
                    string += symbol
                #     for char in string:
                #         if(char=="."):
                #             foundPoint=True
                # if(foundPoint==False):
            return string

    @staticmethod
    def delete_last_character_of_string(string):
        return string[:-1]

    @staticmethod
    def return_result_of_extraction_of_the_root(string):
        numbers = [
            '0', '1', '2',
            '3', '4', '5',
            '6', '7', '8',
            '9'
        ]
        lastCharOfStringIsNumber = False
        if len(string) > 0:
            for number in numbers:
                if (string[-1] == number):
                    lastCharOfStringIsNumber = True
            if (lastCharOfStringIsNumber == True):
                value = eval(string)
                string = math.sqrt(value)

        if lastCharOfStringIsNumber == True:
            return str(round(string, 5))
        else:
            return string

    @staticmethod
    def sum_the_value(string):
        numbers = [
            '0', '1', '2',
            '3', '4', '5',
            '6', '7', '8',
            '9'
        ]
        lastCharOfStringIsNumber = False
        if len(string) > 0:
            for number in numbers:
                if (string[-1] == number):
                    lastCharOfStringIsNumber = True
            if (lastCharOfStringIsNumber):
                string = eval(string)
        string = str(string)
        if string[-2] == '.' and string[-1] == '0':
            string = string[:-2]
        return str(string)