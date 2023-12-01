from common import *
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    string_to_digit = {
        "one":      "1",
        "two":      "2",
        "three":    "3",
        "four":     "4",
        "five":     "5",
        "six":      "6",
        "seven":    "7",
        "eight":    "8",
        "nine":     "9",
    }

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        # this regex uses "lookahead" to capture overlapping strings
        # example: "8oneightgp" should return "8" and "eight", but without lookahead
        # it returns "8" and "one", because when the regex matches "one", it
        # consumes the characters, and the remaining string is only "ightgp", which doesn't match anything.
        # Lookahead allows you to find all starting positions for matching strings, without consuming them.
        regex_pattern = r"(?=(\d|" + "|".join(self.string_to_digit.keys()) + "))"
        total = 0

        for cur_line in file_lines:
            cur_match_list = re.findall(regex_pattern, cur_line)
            first_num = cur_match_list[0]
            last_num = cur_match_list[-1]

            if first_num in self.string_to_digit:
                first_num = self.string_to_digit[first_num]

            if last_num in self.string_to_digit:
                last_num = self.string_to_digit[last_num]

            total += int(first_num + last_num)

        return total


p2 = Part_2()
p2.test(142, [("example_2", 281)])
p2.execute()
