from common import *

# Workflow references are organized as a tree, so there are no loops and all leaves are terminating states (A or R)
# From the example:
#   in
#       px
#           qkq
#               A
#               crn
#                   A
#                   R
#           A
#           rfg
#               gd
#                   R
#               R
#               A
#       qqz
#           qs
#               A
#               hx
#                   A
#           hdj
#               A
#               pv
#                   R
#                   A
#           R


def get_empty_set():
    return {"x": set(), "m": set(), "a": set(), "s": set()}


def union_set(set_a, set_b):
    return {
        "x": set_a["x"] | set_b["x"],
        "m": set_a["m"] | set_b["m"],
        "a": set_a["a"] | set_b["a"],
        "s": set_a["s"] | set_b["s"],
    }


def get_accepted_set(starting_set, workflow_dict, cur_workflow_name, level):

    for set_to_check in starting_set.values():
        if len(set_to_check) == 0:
            return get_empty_set()

    if cur_workflow_name == "A":
        # All starting values are accepted
        return starting_set
    if cur_workflow_name == "R":
        # All starting values are rejected
        return get_empty_set()

    cur_workflow = workflow_dict[cur_workflow_name]
    result_set = get_empty_set()

    for cur_rule in cur_workflow:

        if len(cur_rule) == 1:
            new_set = get_accepted_set(starting_set, workflow_dict, cur_rule[0], level+1)
            result_set = union_set(result_set, new_set)
        else:
            part_name, comparison_symbol, target, new_workflow_name = cur_rule
            set_if_true = {x for x in starting_set[part_name] if (x > target and comparison_symbol == ">") or (x < target and comparison_symbol == "<")}
            set_if_false = {x for x in starting_set[part_name] if (x <= target and comparison_symbol == ">") or (x >= target and comparison_symbol == "<")}

            starting_set[part_name] = set_if_true
            new_set = get_accepted_set(starting_set, workflow_dict, new_workflow_name, level+1)
            result_set = union_set(result_set, new_set)
            starting_set[part_name] = set_if_false

    return result_set


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        workflow_list, _ = [x.split("\n") for x in open_file(filepath).split("\n\n")]

        # Dictionary of workflows:
        #   - Key: workflow name
        #   - Value: array of instructions
        #               Each instruction is an array of strings:
        #                   -   four strings for a normal instruction
        #                           (category, comparison symbol, value, next workflow)
        #                   -   a single string for A and R instructions
        workflow_dict = {}
        for cur_workflow in workflow_list:
            workflow_name, workflow_instruction_str = cur_workflow[:-1].split("{")
            workflow_dict[workflow_name] = []
            for instruction in workflow_instruction_str.split(","):
                if ":" in instruction:
                    category = instruction[0]
                    comparison_symbol = instruction[1]
                    value, next_workflow = instruction[2:].split(":")
                    value = int(value)

                    processed_instruction = [category, comparison_symbol, value, next_workflow]
                else:
                    processed_instruction = [instruction]
                workflow_dict[workflow_name].append(processed_instruction)

        starting_set = {
            "x": set(range(1, 4001)),
            "m": set(range(1, 4001)),
            "a": set(range(1, 4001)),
            "s": set(range(1, 4001))
        }

        result_set = get_accepted_set(starting_set, workflow_dict, "in", 0)
        possible_x = len(result_set["x"])
        possible_m = len(result_set["m"])
        possible_a = len(result_set["a"])
        possible_s = len(result_set["s"])

        return possible_x * possible_m * possible_a * possible_s


p2 = Part_2()
p2.test(167409079868000)
p2.execute()
