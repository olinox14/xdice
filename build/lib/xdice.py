'''
    xdice is a lightweight python 3.3+ library for managing rolls of dice.

    License: GNU

@author: Olivier Massot <croki.contact@gmail.com>, 2017
'''
import random
import re

__VERSION__ = "1.2.3"

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

def rolldice(faces, amount=1, drop_lowest=0, drop_highest=0):
    """
    > Similar to xdice.Dice(faces, amount).roll()
    """
    return Dice(faces, amount, drop_lowest, drop_highest).roll()

_ALLOWED = {'abs': abs, 'max': max, 'min': min}

def _secured_eval(raw):
    """ securely evaluate the incoming raw string
    by avoiding the use of any non-allowed function """
    return eval(raw, {"__builtins__":None}, _ALLOWED)

def _assert_int_ge_to(value, threshold=0, msg=""):
    """ assert value is an integer greater or equal to threshold """
    try:
        if int(value) < threshold:
            raise ValueError()
    except (TypeError, ValueError):
        raise ValueError(msg)

def _pop_lowest(lst):
    """ pop the lowest value from the list
    return the popped value"""
    return lst.pop(lst.index(min(lst)))

def _pop_highest(lst):
    """ pop the highest value from the list
    return a tuple (new list, popped value)"""
    highest = lst.pop(lst.index(max(lst)))
    return highest

def _normalize(pattern):
    return str(pattern).replace(" ", "").lower().replace("d%", "d100")

class Dice():
    """
    Dice(sides, amount=1):
    Set of dice.

    Use roll() to get a Score() object.
    """
    DEFAULT_SIDES = 20
    DICE_RE_STR = r"(?P<amount>\d*)d(?P<sides>f|\d*)(?:l(?P<lowest>\d*))?(?:h(?P<highest>\d*))?([x!])?"
    DICE_RE = re.compile(DICE_RE_STR)

    def __init__(self, sides, amount=1, drop_lowest=0, drop_highest=0, explode=False):
        """ Instantiate a Die object """
        self._sides = 1
        self._amount = 0
        self._drop_lowest = 0
        self._drop_highest = 0
        self._explode = explode

        self.sides = sides
        self.amount = amount
        self.drop_lowest = drop_lowest
        self.drop_highest = drop_highest

    @property
    def sides(self):
        """ Number of faces of the dice """
        return self._sides

    @sides.setter
    def sides(self, sides):
        """ Set the number of faces of the dice """
        if sides != "f":
            _assert_int_ge_to(sides, 1, "Invalid value for sides ('{}')".format(sides))
            sides = int(sides)
        self._sides = sides

    @property
    def amount(self):
        """ Amount of dice """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """ Set the amount of dice """
        _assert_int_ge_to(amount, 0, "Invalid value for amount ('{}')".format(amount))
        self._amount = amount

    @property
    def drop_lowest(self):
        """ The amount of lowest dices to ignore """
        return self._drop_lowest

    @drop_lowest.setter
    def drop_lowest(self, drop_lowest):
        """ Set the amount of lowest dices to ignore """
        _assert_int_ge_to(drop_lowest, 0, "Invalid value for drop_lowest ('{}')".format(drop_lowest))
        if self.drop_highest + drop_lowest > self.amount:
            raise ValueError("You can not drop more dice than amount")
        self._drop_lowest = drop_lowest

    @property
    def drop_highest(self):
        """ The amount of highest dices to ignore """
        return self._drop_highest

    @drop_highest.setter
    def drop_highest(self, drop_highest):
        """ Set the amount highest dices to ignore """
        _assert_int_ge_to(drop_highest, 0, "Invalid value for drop_highest ('{}')".format(drop_highest))
        if self.drop_lowest + drop_highest > self.amount:
            raise ValueError("You can not drop more dice than amount")
        self._drop_highest = drop_highest

    @property
    def explode(self):
        """ Should the dice 'explode'
        'Explode' means each maximal score will trigger a new roll.
        The resulting score will be add to the results.
         """
        return self._explode

    @explode.setter
    def explode(self, explode):
        """ Define if the dice should 'explode' """
        self._explode = explode

    @property
    def name(self):
        """ build the name of the Dice """
        return "{}d{}{}{}{}".format(self._amount,
                                  self._sides,
                                  "l{}".format(self._drop_lowest) if self._drop_lowest else "",
                                  "h{}".format(self._drop_highest) if self._drop_highest else "",
                                  "x" if self._explode else "")

    def __repr__(self):
        """ Return a string representation of the Dice """
        lowstr = "; drop_lowest={}".format(self.drop_lowest) if self.drop_lowest else ""
        highstr = "; drop_highest={}".format(self.drop_highest) if self.drop_highest else ""
        explodestr = "; explode"if self.explode else ""
        fudgestr = "; fudge"if self.sides == "f" else ""
        return "<Dice; sides={}; amount={}{}{}{}{}>".format(self.sides, self.amount, lowstr, highstr, explodestr, fudgestr)

    def __eq__(self, d):
        """
        Eval equality of two Dice objects
        used for testing matters
        """
        return self.sides == d.sides and self.amount == d.amount

    def _rollone(self):
        return random.randint(1, self._sides) if self._sides != "f" else random.randint(-1, 1)

    def roll(self):
        """ Role the dice and return a Score object """
        # Sort results
        results = [self._rollone() for _ in range(self._amount)]
        dropped = [_pop_lowest(results) for _ in range(self._drop_lowest)] + \
                    [_pop_highest(results) for _ in range(self._drop_highest)]
        if self._explode:
            exploded = [self._rollone() for _ in range(len([score for score in results if score == self._sides]))]
            results += exploded
        return Score(results, dropped, self.name)

    @classmethod
    def parse(cls, pattern):
        """ parse a pattern of the form 'xdx', where x are positive integers """
        pattern = _normalize(pattern)

        match = cls.DICE_RE.match(pattern)
        if match is None:
            raise ValueError("Invalid Dice pattern ('{}')".format(pattern))

        amount, sides, lowest, highest, explode = match.groups()

        amount = amount or 1
        sides = sides or cls.DEFAULT_SIDES
        if lowest == "":
            lowest = 1
        lowest = lowest or 0
        if highest == "":
            highest = 1
        highest = highest or 0

        return Dice(*[sides, int(amount), int(lowest), int(highest), bool(explode)])

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
    def __new__(cls, detail, dropped=[], name=""):
        """
        detail should only contain integers
        Score value will be the sum of the list's values.
        """
        score = super(Score, cls).__new__(cls, sum(detail))
        score._detail = detail
        score._dropped = dropped
        score._name = name
        return score

    @property
    def detail(self):
        """ Return the detailed score
        as a list of integers,
        which are the results of each die rolled """
        return self._detail

    def __repr__(self):
        """ Return a string representation of the Score """
        return "<Score; score={}; detail={}; dropped={}; name={}>".format(int(self),
                                                                          self.detail,
                                                                          self.dropped,
                                                                          self.name)

    def __str__(self):
        """Returns a string representation """
        # reimplements standard __str__ method for compatibility with python3.8+
        return str(int(self))

    def format(self, verbose=False):
        """
        Return a formatted string detailing the score of the Dice roll.
        > Eg: '3d6' => '[1,5,6]'
        """
        basestr = str(list(self.detail))
        if not verbose:
            return basestr
        else:
            droppedstr = ", dropped:{}".format(self.dropped) if verbose and self.dropped else ""
            return "{}(scores:{}{})".format(self._name, basestr, droppedstr)

    def __contains__(self, value):
        """ Does score contains the given result """
        return self.detail.__contains__(value)

    def __iter__(self):
        """ Iterate over results """
        return self.detail.__iter__()

    @property
    def dropped(self):
        """ list of dropped results """
        return self._dropped

    @property
    def name(self):
        """ descriptive name of the score """
        return self._name


class Pattern():
    """ A dice-notation pattern """
    RE_REPEAT = re.compile(r"(?:r(\d*)\((.*)\))")

    def __init__(self, instr):
        """ Instantiate a Pattern object. """
        if not instr:
            raise ValueError("Invalid value for 'instr' ('{}')".format(instr))
        self.instr = _normalize(instr)
        self.dices = []
        self.format_string = ""

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

        expandedstr = Pattern.parse_repeat(self.instr)
        self.format_string = Dice.DICE_RE.sub(_submatch, expandedstr)

    def roll(self):
        """
        Compile the pattern if it has not been yet, then roll the dice.
        Return a PatternScore object.
        """
        if not self.format_string:
            self.compile()
        scores = [dice.roll() for dice in self.dices]
        return PatternScore(self.format_string, scores)

    @classmethod
    def parse_repeat(cls, pattern):
        """ parse a pattern to replace the rX(expr) patterns by (expr + ... + expr) [X times] """
        return cls.RE_REPEAT.sub(cls._sub_repeat, pattern)

    @classmethod
    def _sub_repeat(cls, match):
        """ internal """
        repeat, expr = match.groups()
        return "({})".format("+".join([expr for _ in range(int(repeat))]))


class PatternScore(int):
    """
    PatternScore is a subclass of integer, you can then manipulate it as you would do with an integer.
    Moreover, you can get the list of the scores with the score(i)
    or scores() methods, and retrieve a formatted result with the format() method.
    """
    def __new__(cls, eval_string, scores):
        ps = super(PatternScore, cls).__new__(cls, _secured_eval(eval_string.format(*scores)))

        ps._eval_string = eval_string
        ps._scores = scores

        return ps

    def __str__(self):
        """Returns a string representation """
        # reimplements standard __str__ method for compatibility with python3.8+
        return str(int(self))

    def format(self, verbose=False):
        """
        Return a formatted string detailing the result of the roll.
        > Eg: '3d6+4' => '[1,5,6]+4'
        """
        return self._eval_string.format(*[score.format(verbose) for score in self._scores])

    def score(self, i):
        """ Returns the Score object at index i. """
        return self._scores[i]

    def scores(self):
        """ Returns the list of Score objects extracted from the pattern and rolled. """
        return self._scores
