from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        print(open_file(filepath))

        return -1


p2 = Part_2()
p2.test(0)
p2.execute()
