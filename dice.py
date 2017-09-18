'''

'''
import random
import re

_ALLOWED = {'abs': abs}

def roll_d(pattern):
    """ Parse, roll and evaluate the pattern.

    'pattern' can be any mathematics expression and include dice notations ('xDx').
    Eg: '1d4+2', '10d6+2-1d20', '3*(1d6+2)'...Etc

    Returns tuple of score (integer) and detailed result (string)
    """
    # Parse the pattern
    parsed = _parse(pattern)
    raw = _forcejoin(parsed)
    return _secured_eval(raw), raw

def roll(pattern):
    """ Similar to roll_d(), but only return the numeric results (integer) """
    return roll_d(pattern)[0]

def _secured_eval(raw):
    """ securely evaluate the incoming raw string """
    return eval(raw, {"__builtins__":None}, _ALLOWED)

def _forcejoin(obj_list):
    """ force-join the objects of the list by forcing string conversion of its items """
    return "".join(map(str, obj_list))

def _parse(pattern):
    """ split the members and symbols of the pattern and roll them when it is possible """
    return [_roll_if_u_can(m) for m in _split_members(pattern)]

def _normalize(pattern):
    """ normalize the incoming string to a lower string without spaces"""
    return str(pattern).replace(" ", "").lower()

def _split_members(pattern):
    """ split a string by blocks of numeric / symbols / dice notations
    eg: '1d6+2' becomes ['1d6', '+', '2']
    """
    return re.findall(r"[\w']+|[\W']+", _normalize(pattern))

def _roll_if_u_can(member):
    """ try to interpret member as a dice notation and roll it.
    If it can not, member is returned as it was."""
    try:
        return Dice.parse(member).roll()
    except ValueError:
        return member

class Dice():
    """ Dice(sides, amount=1)
    Set of dice. Use roll() to get a score.
    """
    def __init__(self, sides, amount=1):
        self._sides = 1
        self._amount = 0

        self.sides = sides
        self.amount = amount

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, sides):
        try:
            if not int(sides) >= 1:
                raise ValueError()
        except (TypeError, ValueError):
            raise TypeError("Invalid value for sides (given: '{}')".format(sides))
        self._sides = sides

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        try:
            if not int(amount) >= 0:
                raise ValueError()
        except (TypeError, ValueError):
            raise ValueError("Invalid value for amount (given: '{}')".format(amount))
        self._amount = amount

    def roll(self):
        """ Role the dice and return a Score object """
        return Score([random.randint(1, self._sides) for _ in range(self._amount)])

    @classmethod
    def parse(cls, pattern):
        """ parse a pattern of the form 'xdx', where x are positive integers """
        # normalize
        pattern = str(pattern).replace(" ", "").lower()
        # parse
        amount, faces = (int(x) for x in pattern.split("d"))
        # instanciate
        return Dice(faces, amount)

class Score(int):
    """ Score is a subclass of integer.
    Then you can manipulate it as you would do with an integer.

    It also provides an access to the detail with the property 'results'.
    'results' is the list of the scores obtained by each dice.

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
    def __new__(cls, results):
        score = super(Score, cls).__new__(cls, sum(results))
        score._results = results
        return score

    @property
    def results(self):
        return self._results

    def __repr__(self):
        return "<<{} ({})>>".format(int(self), self.results)

    def __contains__(self, value):
        return self.results.__contains__(value)

    def __iter__(self):
        return self.results.__iter__()

# print(roll("2*(2d1+1d1-1d1-3)//2"))
