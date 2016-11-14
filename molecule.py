"""
Parser that parses molecule. It was too late before I found pyparsing, but I
decided to keep using my old parser.
"""
from elements import ELEMENTS


def check(func): # decorator to check state of current_char
    def wrapper(*args):
        if args[0].current_char.isdigit():
            raise Exception("Incorrect syntax")
        elif args[0].current_char.isalpha():
            return func(*args)
        elif not args[0].current_char:
            return 0
        else:
            raise Exception("Incorrect syntax")
    return wrapper


class MoleculeParser(object):
    def __init__(self, molecule):
        self.molecule = molecule
        self.index = 0
        self.current_char = self.molecule[self.index]

    def parse(self):
        self.parsed_molecule = []
        while True:
            self.current = self.get_element()
            if not self.current:
                break
            self.parsed_molecule.append(self.current)

        return self.parsed_molecule

    def get_integer(self):
        integer = ""
        while self.current_char.isdigit():
            integer += self.current_char
            self.advance()
        return integer

    @check
    def get_element(self):
        element = ""
        counter_check = 0
        while self.current_char.isalpha() and counter_check < 2:
            if counter_check == 0 and self.current_char.islower(): # if the first letter of an element is lowercase
               raise Exception("Incorrect syntax")
            if not(counter_check > 0 and self.current_char.isupper()): #  if the parser is on the first letter and is
                element += self.current_char                           #  uppercase, the parser is on the second letter
                self.advance()                                         #  and is lowercase, or both are false
            counter_check += 1                                         #  (counter_check > 0 or self.current_char.isupper() doesn't work)

        amount = self.get_integer()

        return (element, amount)

    def advance(self):
        if self.index < len(self.molecule)-1:
            self.index += 1
            self.current_char = self.molecule[self.index]
        else:
            self.current_char = ""

def get_molarmass(molecule):
    parser = MoleculeParser(molecule)
    tuples = parser.parse()
    total = 0
    for element, amount in tuples:
        amount = int(amount if amount else 1)
        try:
            total += ELEMENTS[element].mass * amount
        except KeyError:
            raise Exception("Bad element name")
    return total
