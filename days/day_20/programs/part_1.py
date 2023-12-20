from common import *


class Module:
    name = ""
    output_list = []

    def __init__(self, init_string: str):
        self.name, output_str = init_string.split(" -> ")
        self.output_list = output_str.split(", ")

    def get_pulse(self, pulse: (str, bool)) -> list[(str, str, bool)]:
        raise NotImplementedError('Method "get_pulse" not implemented.')


class Broadcaster(Module):

    def __init__(self, init_string):
        super().__init__(init_string)

    def get_pulse(self, pulse: (str, bool)) -> list[(str, str, bool)]:
        return [(self.name, output, pulse[1]) for output in self.output_list]


class FlipFlop(Module):

    cur_state = False

    def __init__(self, init_string):
        super().__init__(init_string)
        self.cur_state = False

    def get_pulse(self, pulse: (str, bool)) -> list[(str, str, bool)]:
        if pulse[1]:
            return []

        self.cur_state = not self.cur_state
        return [(self.name, output, self.cur_state) for output in self.output_list]


class Conjunction(Module):

    last_pulse_dict = {}

    def __init__(self, init_string):
        super().__init__(init_string)
        self.last_pulse_dict = {}

    def add_input(self, input_name):
        self.last_pulse_dict[input_name] = False

    def get_pulse(self, pulse: (str, bool)) -> list[(str, str, int)]:
        input_name, pulse_val = pulse
        self.last_pulse_dict[input_name] = pulse_val

        is_low_pulse = False in self.last_pulse_dict.values()

        return [(self.name, output, is_low_pulse) for output in self.output_list]


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        module_dict = {}

        for file_line in open_file_lines(filepath):
            if file_line[0] == "%":
                new_flip_flop = FlipFlop(file_line[1:])
                module_dict[new_flip_flop.name] = new_flip_flop
            elif file_line[0] == "&":
                new_conjunction = Conjunction(file_line[1:])
                module_dict[new_conjunction.name] = new_conjunction
            else:
                new_broadcaster = Broadcaster(file_line)
                module_dict[new_broadcaster.name] = new_broadcaster

        # Initialize input of all Conjunction modules
        for cur_module in module_dict.values():
            if type(cur_module) == Conjunction:
                for input_module in [input_module.name for input_module in module_dict.values() if cur_module.name in input_module.output_list]:
                    cur_module.add_input(input_module)

        high_pulse_count = 0
        low_pulse_count = 0

        for i in range(1000):
            pulse_list = [("button", "broadcaster", False)]

            while len(pulse_list) > 0:
                cur_pulse = pulse_list.pop(0)
                last_module_name, cur_module_name, cur_pulse_val = cur_pulse

                if cur_pulse_val:
                    high_pulse_count += 1
                else:
                    low_pulse_count += 1

                if cur_module_name not in module_dict:
                    continue

                pulse_list += module_dict[cur_module_name].get_pulse((last_module_name, cur_pulse_val))

        return high_pulse_count * low_pulse_count


p1 = Part_1()
p1.test(32000000, [("example_2.txt", 11687500)])
p1.execute()
