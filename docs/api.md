# API

#### xdice.compile(pattern_string)

> Similar to`xdice.Pattern(pattern_string).compile()`

Returns a compiled Pattern object.

Pattern object can then be rolled to obtain a PatternScore object.

#### xdice.roll(pattern_string)

> Similar to`xdice.Pattern(pattern_string).roll()`

#### xdice.rolldice(faces, amount=1)

> Similar to`xdice.Dice(faces, amount).roll()`

## `Dice` object

Set of dice.

#### Dice.__init__(sides, amount=1)

Instantiate a set of dice.

#### dice.roll()

Role the dice and return a Score object

####*[classmethod]* Dice.parse(cls, pattern)

Parse a pattern of the form 'AdX', where A and X are positive integers.
Returns the corresponding Dice object.

## `Score` object

Score is a subclass of integer, you can then manipulate it as you would do with an integer.

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

#### Score.__new__(iterable)

>`iterable` should only contain integers

Score value will be the sum of the list's values.


## `Pattern` object

Dice notation pattern.

#### Pattern.__init__(instr)

Instantiate a Pattern object.

#### pattern.compile()

Parse the pattern. Two properties are updated at this time:

* *pattern.format_string*

The ready-to-be-formatted string built from the `instr` argument.

> Eg: "1d6+4+1d4" => "{0}+4-{1}"

 
* *pattern.dices*

The list of parsed dice.

> Eg: "1d6+4+1d4" => [<Dice; sides=6;amount=1>, <Dice; sides=4;amount=1>]

#### pattern.roll()

Compile the pattern if it has not been yet, then roll the dice.

Return a PatternScore object.

## `PatternScore` object

PatternScore is a subclass of **integer**, you can then manipulate it as you would do with an integer.

Moreover, you can get the list of the scores with the score(i) or scores() methods, and retrieve a formatted result with the format() method.

#### pattern_score.scores()

Returns the list of Score objects extracted from the pattern and rolled.

#### pattern_score.score(i)

Returns the Score object at index i.

#### pattern_score.format()

Return a formatted string detailing the result of the roll.

> Eg: '3d6+4' => '[1,5,6]+4'


