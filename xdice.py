'''
    xdice is a lightweight python 3.3+ library for managing rolls of dice.

    License: GNU

@author: Olivier Massot <croki.contact@gmail.com>, 2017
'''
import random
import re

__VERSION__ = 1.0

# TODO: 'L', 'LX', 'H' and 'HX' notations: drop the x lowest or highest results => eg: 'AdXl3'
# TODO: (?) 'Rx(...)' notation: roll x times the pattern in the parenthesis => eg: R3(1d4+3)
# TODO: 'd%' notation: d% <=> d100
# TODO: (?) Dice pools, 6-sided variations, 10-sided variations,
# Open-ended variations (https://en.wikipedia.org/wiki/Dice_notation)

def compile(pattern_string):  # @ReservedAssignment
    """
    > Similar to xdice.Pattern(pattern_string).compile()
    Returns a compiled Pattern object.
    Pattern object can then be rolled to obtain a PatternScore object.
    """
    pattern = Pattern(pattern_string)
    pattern.compile()
    return pattern

def roll(pattern_string):
    """
    > Similar to xdice.Pattern(pattern_string).roll()
    """
    return Pattern(pattern_string).roll()

def rolldice(faces, amount=1):
    """
    > Similar to xdice.Dice(faces, amount).roll()
    """
    return Dice(faces, amount).roll()

_ALLOWED = {'abs': abs, 'max': max, 'min': min}

def _secured_eval(raw):
    """ securely evaluate the incoming raw string
    by avoiding the use of any non-allowed function """
    return eval(raw, {"__builtins__":None}, _ALLOWED)

class Dice():
    """
    Dice(sides, amount=1):
    Set of dice.

    Use roll() to get a Score() object.
    """
    DEFAULT_SIDES = 20

    def __init__(self, sides, amount=1):
        """ Instanciate a Die object """
        self._sides = 1
        self._amount = 0

        self.sides = sides
        self.amount = amount

    @property
    def sides(self):
        """ Number of faces of the dice """
        return self._sides

    @sides.setter
    def sides(self, sides):
        """ Set the number of faces of the dice """
        try:
            if int(sides) < 1:
                raise ValueError()
        except (TypeError, ValueError):
            raise ValueError("Invalid value for sides (given: '{}')".format(sides))
        self._sides = sides

    @property
    def amount(self):
        """ Amount of dice """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """ Set the amount of dice """
        try:
            if int(amount) < 0:
                raise ValueError()
        except (TypeError, ValueError):
            raise ValueError("Invalid value for amount (given: '{}')".format(amount))
        self._amount = amount

    def __repr__(self):
        """ Return a string representation of the Dice """
        return "<Dice; sides={}; amount={}>".format(self.sides, self.amount)

    def __eq__(self, d):
        """
        Eval equality of two Dice objects
        used for testing matters
        """
        return self.sides == d.sides and self.amount == d.amount

    def roll(self):
        """ Role the dice and return a Score object """
        return Score([random.randint(1, self._sides) for _ in range(self._amount)])

    @classmethod
    def parse(cls, pattern):
        """ parse a pattern of the form 'xdx', where x are positive integers """
        pattern = str(pattern).replace(" ", "").lower()

        amount, sides = pattern.split("d")
        if not amount:
            amount = 1
        if not sides:
            sides = cls.DEFAULT_SIDES

        return Dice(*map(int, [sides, amount]))

class Score(int):
    """ Score is a subclass of integer.
    Then you can manipulate it as you would do with an integer.

    It also provides an access to the detailed score with the property 'detail'.
    'detail' is the list of the scores obtained by each dice.

    Score class can also be used as an iterable, to walk trough the individual scores.

    eg:
        >>> s = Score([1,2,3])
        >>> print(s)
        6
        >>> s + 1
        7
        >>> list(s)
        [1,2,3]

    """
    def __new__(cls, detail):
        """
        detail should only contain integers
        Score value will be the sum of the list's values.
        """
        score = super(Score, cls).__new__(cls, sum(detail))
        score._detail = detail
        return score

    @property
    def detail(self):
        """ Return the detailed score
        as a list of integers,
        which are the results of each die rolled """
        return self._detail

    def __repr__(self):
        """ Return a string representation of the Score """
        return "<Score; score={}; detail={}>".format(int(self), self.detail)

    def __contains__(self, value):
        """ Does score contains the given result """
        return self.detail.__contains__(value)

    def __iter__(self):
        """ Iterate over results """
        return self.detail.__iter__()

class Pattern():
    """ A dice-notation pattern """
    def __init__(self, instr):
        """ Instantiate a Pattern object. """
        if not instr:
            raise ValueError("Invalid value for 'instr' ('{}')".format(instr))
        self.instr = Pattern._normalize(instr)
        self.dices = []
        self.format_string = ""

    @staticmethod
    def _normalize(instr):
        """ normalize the incoming string to a lower string without spaces"""
        return str(instr).replace(" ", "").lower()

    def compile(self):
        """
        Parse the pattern. Two properties are updated at this time:

        * pattern.format_string:
        The ready-to-be-formatted string built from the instr argument.
        > Eg: '1d6+4+1d4' => '{0}+4-{1}'

        * pattern.dices
        The list of parsed dice.
        > Eg: '1d6+4+1d4' => [(Dice; sides=6;amount=1), (Dice; sides=4;amount=1)]
        """
        def _submatch(match):
            dice = Dice.parse(match.group(0))
            index = len(self.dices)
            self.dices.append(dice)
            return "{{{}}}".format(index)

        self.format_string = re.sub(r'\d*d\d*', _submatch, self.instr)

    def roll(self):
        """
        Compile the pattern if it has not been yet, then roll the dice.
        Return a PatternScore object.
        """
        if not self.format_string:
            self.compile()
        scores = [dice.roll() for dice in self.dices]
        return PatternScore(self.format_string, scores)

class PatternScore(int):
    """
    PatternScore is a subclass of integer, you can then manipulate it as you would do with an integer.
    Moreover, you can get the list of the scores with the score(i) or scores() methods, and retrieve a formatted result with the format() method.
    """
    def __new__(cls, eval_string, scores):
        ps = super(PatternScore, cls).__new__(cls, _secured_eval(eval_string.format(*scores)))

        ps._eval_string = eval_string
        ps._scores = scores

        return ps

    def format(self):
        """
        Return a formatted string detailing the result of the roll.
        > Eg: '3d6+4' => '[1,5,6]+4'
        """
        return self._eval_string.format(*[str(list(score)) for score in self._scores])

    def score(self, i):
        """ Returns the Score object at index i. """
        return self._scores[i]

    def scores(self):
        """ Returns the list of Score objects extracted from the pattern and rolled. """
        return self._scores
