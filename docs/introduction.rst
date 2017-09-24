XDice
=====

Presentation
------------

*xdice* is a lightweight python library for managing dice, scores, and
dice-notation patterns.

It allows to easily interpret literal expressions as rolls of dice
(‘1d6’, ‘3d4+3’, ‘12d6+1d4’…etc.), then manipulate the results.

Python Versions
~~~~~~~~~~~~~~~

DiceRollParser has been tested with python 3.3+

Examples
~~~~~~~~

::

    import dice

    # Roll dices with dice.rolldice()

    score = dice.rolldice(6, amount=2)

    # manipulate 'score' as an integer

    print(score)
    >> 11
    print(score * 2)
    >> 22
    print(score == 11)
    >> True

    # Or iterate over the results

    for result in score:
        print(result)
    >> 5
    >> 6

    # Parse patterns with dice.roll()

    ps = dice.roll("2d6+18")

    print(ps)
    >> 28
    print(ps.format())
    >> '[5,6]+18'

    ps = dice.roll("6D%L2")

    print(ps)
    >> 315
    print(ps.format(verbose=True))
    >> '6D%L2(scores:[80, 70, 76, 89], dropped:[2, 49])'

Contribution
~~~~~~~~~~~~

Any opinion / contribution is welcome, please contact us.

Installation
~~~~~~~~~~~~

::

    pip install xdice

License
~~~~~~~

*xdice* is under GNU License

Tags
~~~~

::

    dice roll d20 game random parser dices role board