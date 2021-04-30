import random
from contestant import Contestant

contestant = Contestant('', '', '', '')


class Sweepstakes:
    def __init__(self, name):
        self.winner = name
        self.contestant = {}
        self.name = name

    def register_contestant(self, registered_contestant):
        self.input('Enter your info')
        key = len(self.contestant) + 1
        self.contestant[key] = registered_contestant

    def pick_winner(self, name, registered_contestant):
        self.winner = (name.random.choice(registered_contestant))
        print(f'And the winner is {self.winner.first_name} {self.winner.last_name}!!')

    def print_contestant_info(self, registered_contestant):
        print(registered_contestant.first_name)
        print(registered_contestant.last_name)
        print(registered_contestant.email_address)
        print(registered_contestant.registration_number)

    def input(self, registered_contestant):
        pass
