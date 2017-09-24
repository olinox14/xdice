API Reference
=============

Import the *xdice* library with `import dice`

The dice module
---------------

dice.compile(pattern\_string)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Similar to `xdice.Pattern(pattern_string).compile()`

dice.roll(pattern\_string)
^^^^^^^^^^^^^^^^^^^^^^^^^^

    Similar to `xdice.Pattern(pattern_string).roll()`

dice.rolldice(faces, amount=1, drop\_lowest=0, drop\_highest=0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Similar to `xdice.Dice(faces, amount, drop_lowest, drop_highest).roll()`

Dice class
----------

    Set of dice.

Dice.__init__ (sides, amount=1, drop\_lowest=0, drop\_highest=0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Instantiate a set of dice.

Properties
^^^^^^^^^^

-  `dice.sides`: number of sides of the dice
-  `dice.amount`: amount of dice to roll
-  `dice.drop_lowest`: amount of lowest scores to drop
-  `dice.drop_highest`: amount of highest scores to drop
-  `dice.name` : Descriptive name of the Dice object

dice.roll()
^^^^^^^^^^^

    Role the dice and return a Score object

*[classmethod]* Dice.parse(cls, pattern)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Parse a pattern of the form ‘AdX’, where A and X are positive
    integers, then return the corresponding Dice object. Use
    ‘AdX[Ln][Hn]’ to drop the n lowest and/or highest dice when rolled.


Score class
-----------

    Score is a subclass of integer, you can then manipulate it as you
    would do with an integer.

    | It also provides an access to the detailed score with the property
      ‘detail’.
    | ‘detail’ is the list of the scores obtained by each dice.

    Score class can also be used as an iterable, to walk trough the
    individual scores.

::

    eg:
        >>> s = Score([1,2,3])
        >>> print(s)
        6
        >>> s + 1
        7
        >>> list(s)
        [1,2,3]

Score.__new__(iterable, dropped=[], name='')
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    `iterable` should only contain integers

    Score value will be the sum of the list’s values.

Properties
^^^^^^^^^^

-  `score.detail`: similar to list(score), return the list of the individual results
-  `score.name`: descriptive name of the dice rolled
-  `score.dropped`: list of the dropped results

score.format(verbose=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    A formatted string describing the detailed result.

Pattern class
-------------

    Dice notation pattern.

Pattern.__init__ (instr)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Instantiate a Pattern object.

pattern.compile()
^^^^^^^^^^^^^^^^^

    Parse the pattern. Two properties are updated at this time:

-  *pattern.format\_string*

    The ready-to-be-formatted string built from the ``instr`` argument.

    *Eg: ‘1d6+4+1d4’ => ‘{0}+4-{1}’*

-  *pattern.dices*

    The list of parsed dice.

    *Eg: ‘1d6+4+1d4’ => [(Dice; sides=6;amount=1), (Dice;
    sides=4;amount=1)]*

pattern.roll()
^^^^^^^^^^^^^^

    Compile the pattern if it has not been yet, then roll the dice.

    Return a PatternScore object.

PatternScore class
-------------------

    PatternScore is a subclass of **integer**, you can then manipulate
    it as you would do with an integer.

    Moreover, you can get the list of the scores with the score(i) or
    scores() methods, and retrieve a formatted result with the format()
    method.

pattern\_score.scores()
^^^^^^^^^^^^^^^^^^^^^^^

    Returns the list of Score objects extracted from the pattern and
    rolled.
    
pattern\_score.format(verbose=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    A formatted string describing the detailed result.
