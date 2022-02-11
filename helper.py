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
        if symbol != ".":
            if symbol != "0":
                if len(string) > 0:
                    for number in numbers:
                        if string[-1] == number:
                            string += symbol
                return string
            if symbol == "0":
                string += symbol
                return string

        if symbol == ".":
            last_char_of_string_is_number = False
            if len(string) > 0:
                for number in numbers:
                    if string[-1] == number:
                        last_char_of_string_is_number = True
                if last_char_of_string_is_number is True:
                    string += symbol
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
        last_char_of_string_is_number = False
        if len(string) > 0:
            for number in numbers:
                if string[-1] == number:
                    last_char_of_string_is_number = True
            if last_char_of_string_is_number is True:
                value = eval(string)
                string = math.sqrt(value)

        if last_char_of_string_is_number is True:
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
        last_char_of_string_is_number = False
        if len(string) > 0:
            for number in numbers:
                if string[-1] == number:
                    last_char_of_string_is_number = True
            if last_char_of_string_is_number:
                string = eval(string)
        string = str(string)
        if string[-2] == '.' and string[-1] == '0':
            string = string[:-2]
        return str(string)