import random
from contestant import Contestant

contestant = Contestant('', '', '', '')


class Sweepstakes:
    def __init__(self, name):
        self.contestant = {}
        self.name = name

    def register_contestant(self, contestant):
        key = len(self.contestant_list) + 1
        self.contestant_list[key] = contestant

    def pick_winner(self, contestant):
        print(random.choice(contestant))

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
        print(contestant.registration_number)
