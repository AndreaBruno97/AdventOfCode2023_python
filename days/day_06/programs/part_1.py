from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        print(open_file(filepath))

        return -1


p1 = Part_1()
p1.test(0)
p1.execute()
