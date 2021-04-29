from data_stack import Stack


class Stack_manager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self):
        return self.stack.pop()


