from common import *
import re
import math

"""
This solution models the problem in a mathematical form:
the distance d travelled by the boat each round is defined by:
- T: the round's total time
- D: the record distance we have to beat
- t1: the time we hold the button
- t2: the time the boat actually travels (note that T = t1 + t2)
The formula is:         d = speed * travel_time
where the speed is numerically equal to the number of seconds we press the button (t1)
and the travel time is t2. So:
    d = t1 * t2 = t1 * (T - t1) = (T * t1) - t1^2
We also have to count the integer values that satisfy d > D, then we need to find the roots of 
    (T * t1) - t1^2 > D         =>
    -t1^2 + (T * t1) - D > 0    =>
    t1^2 - (T * t1) + D < 0

Using the quadratic formula, the roots have form (T +- delta)/2, but we are only interested in the difference
between their integer approximation:
    floor(x2) - ceiling(x1)     =>
    floor((T + delta)/2) - ceiling((T - delta)/2)

In order to avoid additional comparisons in the code to account for the cases in which
the roots are already integers (we would count them as beating the maximum, when they instead only match it),
instead of considering D the distance given by the input, we consider a larger distance D', with a small increment:
    D' = D + 0.01
"""


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        time_str, distance_str = open_file_lines(filepath)

        time_str = re.sub(r"Time:\s+", "", time_str)
        distance_str = re.sub(r"Distance:\s+", "", distance_str)
        cur_time = int(re.sub(r"\s+", "", time_str))
        cur_max_dist = int(re.sub(r"\s+", "", distance_str))

        new_max_dist = cur_max_dist + 0.01
        delta = ((cur_time ** 2) - (4 * new_max_dist)) ** 0.5
        max_winning_time = math.floor((cur_time + delta) / 2)
        min_winning_time = math.ceil((cur_time - delta) / 2)

        winning_times = max_winning_time - min_winning_time + 1

        return winning_times


p2 = Part_2()
p2.test(71503)
p2.execute()
